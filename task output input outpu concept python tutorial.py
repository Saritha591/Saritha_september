Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
============= RESTART: D:/task input and output python tutorial.py =============
>>> year = 2016
... event= 'good'
... f'result of the {year} {event}'
SyntaxError: multiple statements found while compiling a single statement
>>> year = 2020
>>> event = 'excellent'
>>> f'results of the{year} {event}'
'results of the2020 excellent'
>>> yes_votes = 153000
>>> no_votes = 4000
>>> percentage = yes_votes/(yes_votes+no_votes)
>>> '{-10} yes votes {:2.2%}.format(yes_votes,percentage)
SyntaxError: unterminated string literal (detected at line 1)
>>> yes_votes = 153000
... no_votes = 4000
... percentage = yes_votes/(yes_votes+no_votes)
... '{-10} yes votes {:2.2%}'.format(yes_votes,percentage)
SyntaxError: multiple statements found while compiling a single statement
>>> yes_votes=15300
... no_votes=4000
... percentage = yes_votes/(yes_votes+ no_votes)
... '{-10} yes votes {:2.2%}'.format(yes_votes,percentage)
SyntaxError: multiple statements found while compiling a single statement
>>> s='hello,world'
>>> str(s)
'hello,world'
>>> repr(s)
"'hello,world'"
>>> str(1/7)
'0.14285714285714285'
>>> repr(1/7)
'0.14285714285714285'
>>> x=10 * 3.35
>>> y=200* 200
>>> s='the value of x is' + repr(x)+',and y is '+repr(y)+ '...'
>>> print(s)
the value of x is33.5,and y is 40000...
>>> hello='hello,world\n'
hello=repr(hello)
print(hello)
'hello,world\n'
import math
print(f'the value of pi is approximately {math.pi:.3f}.')
the value of pi is approximately 3.142.
the value of pi is approximately 3.142.
SyntaxError: invalid syntax
table={'sari': 3212, 'chandu': 3215, 'devi': 4567}
for name,phone in table.items( ):
    print(f'{name:10} ==> {phone:10d}')

    
sari       ==>       3212
chandu     ==>       3215
devi       ==>       4567

animals='Bujji'
print(f'my humble suggestion of{animals}.')
my humble suggestion ofBujji.
birds='parrot'
print(f'my happieness is{birds}.')
my happieness isparrot.
print(f'my happieness is{birds!r}.')
my happieness is'parrot'.
bugs='ant'
count=5
area='room'
print(f'debugging{bugs=} {area=}')
debuggingbugs='ant' area='room'
print('we are the{ } who say '{}!''.format('knights','ni'))
SyntaxError: invalid syntax. Perhaps you forgot a comma?
print('we are the{ } who say "{}!"'.format('knights','ni'))
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    print('we are the{ } who say "{}!"'.format('knights','ni'))
KeyError: ' '
print('{0} and {1}'('spam','eggs'))
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    print('{0} and {1}'('spam','eggs'))
TypeError: 'str' object is not callable
str = ('spam','eggs')
str = ('spam','eggs')
print('{0} and {1}'('spam','eggs'))
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    print('{0} and {1}'('spam','eggs'))
TypeError: 'str' object is not callable
str = ('spam','eggs')
print('{0} and {1}'.format('spam','eggs'))
spam and eggs
rint('{1} and {0}'.format('spam','eggs'))
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    rint('{1} and {0}'.format('spam','eggs'))
NameError: name 'rint' is not defined. Did you mean: 'print'?
table = {'sari':2345.'puri':4564,'hari':4567}
SyntaxError: invalid syntax. Perhaps you forgot a comma?
table = {'sari':2345,'puri':4564,'hari':4567}
print('sari: {0[sari]:d};puri: {0[puri]:d} ; hari: {0[hari] :d}'.format(table))
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    print('sari: {0[sari]:d};puri: {0[puri]:d} ; hari: {0[hari] :d}'.format(table))
ValueError: Only '.' or '[' may follow ']' in format field specifier
table = {'sari':2345,'puri':4564,'hari':4567}
print('sari: {0[sari]:d}';'puri: {0[puri]:d}' ; 'hari: {0[hari] :d}'.format(table))
SyntaxError: multiple statements found while compiling a single statement
for x in range(1,11):
    print('{0:2d} {1:3d} {2:4d}'format(x,x*x,x*x*x))
    
SyntaxError: invalid syntax. Perhaps you forgot a comma?
for x in range(1,11):
    print('{0:2d} {1:3d} {2:4d}'.format(x,x*x,x*x*x)


import math
SyntaxError: '(' was never closed
import math
print('the value of pi is approximately %5.3f.'%math.pi)
the value of pi is approximately 3.142.
