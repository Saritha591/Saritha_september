Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x = "hello good moorning all"
>>> print(x)
hello good moorning all
>>> 
>>> name = "chandu"
>>> age= 25
>>> print("my name is" +name +"iam" +age+"years old")
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    print("my name is" +name +"iam" +age+"years old")
TypeError: can only concatenate str (not "int") to str
>>> print("my name is" +name +"iam" +age+"years old")
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    print("my name is" +name +"iam" +age+"years old")
TypeError: can only concatenate str (not "int") to str
>>> print("my name is" +name +"iam" +str(age)+"years old")
my name ischanduiam25years old
>>> #string formatting using string variables
>>> snacks = "biscuits"
>>> time = 4:00
SyntaxError: invalid syntax
>>> snacks = "biscuits"
... time = 4
SyntaxError: multiple statements found while compiling a single statement
>>> snacks="biscuits"
>>> time=4
>>> print("i eat snacks as %s at %d" %(snacks,time))
i eat snacks as biscuits at 4
>>> 
>>> #string formatting with collection types
>>> 
>>> fruits=["apple","grapes","orange"]
>>> print("i love to eat %s and i hate to eat %s also i eat %s" %(fruits[0],fruits[1],fruits[2]))
i love to eat apple and i hate to eat grapes also i eat orange
