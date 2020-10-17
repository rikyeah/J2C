<h1>J2C - Java to C code translator</h1>
<p>
  J2C is a open source project made just for fun: its aim is to try to replicate the structure and behavior of a Java class in the C language.
  Anyone can contribute to it and any addition or fix will be appreciated.
</p>
<h2>Constraints:</h2>
<li>The Java classes have to be syntactically correct</li>
<li>Method overloading is permitted and the translation will work correctly (resulting in multiple functions), but the C result will not compile by C standards</li>
<li>Interface implementation and definition are not supported</li>
<li>Inheritance is not supported</li>
<li>Implicit field resolution is not supported: use <code>this.field</code> instead of <code>field</code> for instance fields and <code>Class.field</code> instead of <code>field</code></li> for class variables</li>
<h3>Details</h3>
<p>Input: A folder or a file (possibly a folder containing .java source files)<br>
  Output: A folder named "translated_foldername" containing the same files as the one in input, except for the .java files, which are translated each in a .h and .c files</p>
  
<p>The parts of the Java class will be translated and written in two separate files, generally a .h for the public parts and a .c for the private parts<p>
