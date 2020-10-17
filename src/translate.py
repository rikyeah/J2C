import re

# regular expressions for java code
access_modifier = "(public|private|protected)?"
identifier = "([a-zA-Z0-9]*)"
method_parameter = identifier + " " + identifier


def removed_methods(class_text):
    """Returns class_text without the text corresponding to the methods' bodies"""
    ret = ''
    skip = 0
    for i in class_text:
        if i == '{':
            skip += 1
        elif i == '}' and skip > 0:
            skip -= 1
        elif skip == 0:
            ret += i
    return ret


def get_import_names(class_text):
    """Returns a list of the names imported by class_text"""
    pattern = re.compile("import [a-zA-Z0-9_.]*;")
    # get just the names of imported classes
    imports = list(map(lambda i: i[7:-1], pattern.findall(class_text)))
    return imports


def get_class_name(class_text):
    """Returns the class name in the class_text"""
    global identifier
    pattern = re.compile("class " + identifier)
    start = pattern.search(class_text).start()
    end = pattern.search(class_text).end()
    return class_text[start + 6:end]


def get_class_fields(class_text):
    """Returns a list of tuples corresponding to all the fields (any modifier, both static and non-static)
    in class_text, in the form (access modifier, type, name, initializer)"""
    global access_modifier
    global identifier
    class_text = class_text[class_text.index("{") + 1:class_text.rfind('}')]
    class_text = removed_methods(class_text)
    # pattern for the fields of the class, optionally initialized
    pattern = re.compile(access_modifier + " ?" + "( ?static )?" + identifier + " " + identifier + " ?(=.*)?;")
    fields_list = pattern.findall(class_text)
    fields = []
    for field in fields_list:
        tmp = {"access modifier": field[0],
               "static": True if field[1] != '' else False,
               "type": field[2],
               "name": field[3],
               "initialization": field[4],
               }
        fields.append(tmp)
    return fields


def get_method_bodies(class_text):
    """Returns a list of all the bodies of the methods in class_text"""
    ret = ""
    skip = 0
    bodies = []
    for char in class_text:
        if skip > 0:  # if skip > 0, it is scanning inside a {} block
            ret += char
        if char == '{':
            skip += 1
        elif char == '}':
            skip -= 1
            if skip == 0:
                bodies.append(ret)
                ret = ""
    return bodies


def get_methods_and_constructors(class_text, class_name):
    method_regex = access_modifier + "( static)?" + " " + identifier + " " + identifier + "(\((.* .*)*\)) ?{"
    constructor_regex = access_modifier + " " + class_name + " ?(\((.* .*)*\)) ?{"
    pattern = re.compile("(" + method_regex + ")|(" + constructor_regex + ")")
    methods = pattern.findall(class_text)
    return methods


def get_class_methods(class_text):
    """Returns a list of dictionaries representing the class_text methods, with the keys:
    is_constructor, access mod, static, return type, name, parameters, body"""
    global access_modifier
    global identifier
    global method_parameter
    class_name = get_class_name(class_text)
    # to avoid wrong matches, just get the class' body
    class_text = class_text[class_text.index("{") + 1:class_text.rfind('}')]
    # class_text = removed_constructors(class_text)
    # get the methods' bodies and signatures
    method_bodies = get_method_bodies(class_text)
    methods_signature = get_methods_and_constructors(class_text, class_name)
    """ elements resulting from the groups matching:
    standard method
    m[0] = full signature
    m[1] = access modifier
    m[2] = static
    m[3] = return type
    m[4] = name
    m[5] = parameters with parentheses
    m[6] = parameters without parentheses
    constructors
    m[7] = full signature
    m[8] = access modifier
    m[9] = parameters with parentheses
    m[10] = parameters without parentheses
    """
    methods = []
    for i, m in enumerate(methods_signature):
        tmp = {"is constructor": False if m[7] == "" else True,
               "access mod": m[1] if m[1] != "" else m[8],
               "static": True if m[2] == " static" else False,
               "return type": m[3] if m[3] != "" else class_name,
               "name": m[4] if m[4] != "" else None,
               "parameters": m[5] if m[5] != "" else m[9],  # or m[6] and m[10]
               "body": method_bodies[i]}
        methods.append(tmp)
    return methods


def translated(class_path):
    """Returns a tuple with the translations of the file at class_path, in the form of
    (public part, private part), corresponding to the interface in the .h file and the .c implementations"""
    public_translation = ""
    private_translation = ""
    # read the text of the whole .java file
    with open(class_path, "r") as classe:
        class_text = classe.read()
    # get information about the class
    class_imports = get_import_names(class_text)
    class_name = get_class_name(class_text)
    class_fields = get_class_fields(class_text)
    class_methods = get_class_methods(class_text)

    # building .h/public translation
    public_translation = build_h_translation(class_name, class_imports, class_methods)

    # build the .c/private translation
    private_translation = build_c_translation(class_name, class_fields, class_methods)
    return public_translation, private_translation


def build_h_translation(class_name, class_imports, class_methods):
    """Returns the translation, meaning the .h header content, of the information given in input"""
    public_translation = ""
    # build ifndef structure to prevent header cyclic inclusion
    public_translation += "#ifndef " + class_name.upper() + "_H\n"
    public_translation += "#define " + class_name.upper() + "_H\n\n"

    # build includes
    for imports in class_imports:
        public_translation += ('#include"' + imports + '.h"\n')

    # build struct forward declaration
    public_translation += "\ntypedef struct " + class_name + " " + class_name + ";\n\n"

    # build public function signatures
    for method in class_methods:
        if method["access mod"] == "public":
            public_translation += method["return type"] if method["return type"] is not None else class_name
            public_translation += " " + (method["name"] if method["name"] is not None else ("new_" + class_name))
            if method["static"] or method["is constructor"]:
                public_translation += method["parameters"] + ";\n"
            else:
                public_translation += "(" + class_name + " this" + (", " if method["parameters"] != "()" else "") + \
                                      method["parameters"][1:] + ";\n"
    # ifndef conclusion
    public_translation += "\n#endif"
    return public_translation


def translate_method_body(code, class_name):
    """Returns the C "translated" version of a java method"""
    # turn method calls in function calls, e.g. this.method(param) becomes method(this, param)

    # just for debugging outputs
    code = code.replace("System.out.printf", "printf")
    code = code.replace("System.out.println", "printf")

    # replace Class.method() in method()
    regex = class_name + "\." + identifier + " ?\("
    pattern = re.compile(regex)
    methods_called = pattern.findall(code)
    for m in methods_called:
        code = re.sub(class_name + "\." + m + " ?\( ?", m + "(", code)

    # replace this.method() in method(this)
    regex = "this" + "\." + identifier + " ?\("
    pattern = re.compile(regex)
    methods_called = pattern.findall(code)
    for m in methods_called:
        code = re.sub("this" + "\." + m + " ?\( ?", m + "(this, ", code)

    # replace instance.method() in method(instance)
    regex = identifier + "\." + identifier + " ?\("
    pattern = re.compile(regex)
    methods_called = pattern.findall(code)
    for m in methods_called:
        print(m)
        print(m[0] + "." + m[1] + "(")
        code = re.sub(m[0] + "\." + m[1] + " ?\( ?", m[1] + "(" + m[0] + ", ", code)

    # turn ClassName.staticField in staticField, as the field is a global variable in the.c file
    for class_field in re.compile("(" + class_name + ")\." + identifier).findall(code):
        code = re.sub(class_field[0] + "." + class_field[1], "static_" + class_field[1], code)

    # turn object creations in function calls to their "constructors" new_ClassName
    code = re.sub("new ", "new_", code)
    return code


def build_c_translation(class_name, class_fields, class_methods):
    """Returns the translation, meaning the .c implementation content, of the information given in input"""
    private_translation = ""

    # build the .h inclusion
    private_translation += '#include"' + class_name + '.h"\n\n'

    # build the instance struct implementation
    private_translation += "// instance fields of the class\n"
    private_translation += ("struct " + class_name + " {\n")
    for field in class_fields:
        if not field["static"]:
            private_translation += ("\t" + " " + field["type"] + " " + field["name"] + ";\n")
    private_translation += "}" + ";\n\n"

    # build the section for the static fields
    private_translation += "// static fields of the class\n"
    for field in class_fields:
        if field["static"]:
            private_translation += (field["type"] + " static_" + field["name"] + ";\n")
    private_translation += "\n"

    # build functions implementations
    for method in class_methods:
        private_translation += method["return type"] if method["return type"] is not None else class_name
        private_translation += " " + (method["name"] if method["name"] is not None else ("new_" + class_name))
        if method["static"] or method["is constructor"]:
            private_translation += method["parameters"]
        else:
            private_translation += "(" + class_name + " this" + (", " if method["parameters"] != "()" else "") + method[
                                                                                                                     "parameters"][
                                                                                                                 1:]
        method["body"] = translate_method_body(method["body"], class_name)
        if method["is constructor"]:
            private_translation += "{\n\t\t" + method["return type"] + " this;" + method["body"][:-2]
            private_translation += "\t\treturn this;\n\t}" + "\n\n"
        else:
            private_translation += "{" + method["body"] + "\n\n"
    return private_translation
