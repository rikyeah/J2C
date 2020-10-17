import os
import shutil

from src.translate import translated


def main(root_directory):
    print(root_directory)
    # root_directory = input("Java project root directory? ")
    # root_directory = "D:/Projects/J2C/tests"
    if os.path.isfile(root_directory):  # if the path indicated is a file, translate and output just that file
        with open(root_directory.replace(".java", ".h"), "w") as current_h_output_file, open(
                root_directory.replace(".java", ".c"), "w") as current_c_output_file:
            (h_translation, c_translation) = translated(root_directory)
            current_h_output_file.write(h_translation)
            current_c_output_file.write(c_translation)
            return
    # explore the project directory recursively, creating mirrored files in translated_<<path>>
    for (root, dirs, files) in os.walk(root_directory, topdown=True):
        # create needed directory (translated_directory)
        os.mkdir(root.replace(os.path.basename(root_directory), "translated_" + os.path.basename(root_directory)))
        for file in files:
            # i/o paths of the files
            input_file_path = os.path.join(root, file)
            output_file_path = os.path.join(
                root.replace(os.path.basename(root_directory), "translated_" + os.path.basename(root_directory)),
                file).replace("/", os.path.sep)
            if file[-5:] == ".java":  # if it is a java file, read it and translate it
                with open(output_file_path.replace(".java", ".h"), "w") as current_h_output_file, open(
                        output_file_path.replace(".java", ".c"), "w") as current_c_output_file:
                    (h_translation, c_translation) = translated(input_file_path)
                    current_h_output_file.write(h_translation)
                    current_c_output_file.write(c_translation)
            else:  # otherwise, just copy the file
                shutil.copy(input_file_path, output_file_path)


if __name__ == "__main__":
    try:
        shutil.rmtree("D:/Projects/J2C/translated_tests")
    except FileNotFoundError:
        pass
    main("D:/Projects/J2C/tests")
