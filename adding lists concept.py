Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # add two list values and store in third list  in python
>>> list1 =[1,2,3]
>>> list2 =[4,5,6]
>>> list =[]
>>> print("list1 value:"list1)
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> print("list1 value:",list1)
list1 value: [1, 2, 3]
>>> print("list2 value:",list2)
list2 value: [4, 5, 6]
>>> for n in range(0,len(list1)):
...     list3.append(list1[n] + list2[n])
...     print("sum of two list:",list3)
... 
...     
Traceback (most recent call last):
  File "<pyshell#10>", line 2, in <module>
    list3.append(list1[n] + list2[n])
NameError: name 'list3' is not defined. Did you mean: 'list1'?
>>> print("sum of two list:",list3)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    print("sum of two list:",list3)
NameError: name 'list3' is not defined. Did you mean: 'list1'?
