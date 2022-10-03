#methods in an array
#append methond:

''''import array
x=array.array('i',[20,30,49,59,35])
print(x)
x.append(60)
print(x)


#count method

import array
x=array.array('i',[45,20,5,5,35,78,30])
c=x.count(400)
print(c)


#extend method:

import array
x=array.array('i',[50,45,60,68])
y=array.array('i',[10,20,30,40])
y.extend(x)
print(y)'''

'''#fromlist method:
import array
list=[50,60,70,80]
print(type(list))
a=array.array('i',[10,20,40,50])
a.fromlist(list)
print(a)

#fromstring method:
import array
str='50,60,56'
a=array.array('i',[3,4,5,6])
a.fromstring(str)
print(a)'''

#Index method:
import array
x=array.array('i',[10,20,30,40,50])
i=x.index(40)
print(i)


#insert method :

import array
x=array.array('i',[300,400,500,600,700])
x.insert(3,150)
print(x)

#pop method:
#particular index given

import array
x=array.array('i',[1,2,4,5,6,7])
x.pop(3)
print(x)

#without index given in pop method

'''import array
x=array.array('i',[1,2,4,5,6,7])
x.pop()
print(x)

#remove method:
import array
x=array.array('i',[100,200,400,500,600,700])
x.remove(500)
print(x)
#it takes exctly one argument

import array
x=array.array('i',[100,200,400,500,600,700])
x.remove( )
print(x)'''

#reverse method

import array
x=array.array('i',[100,200,400,500,600,700])
x.reverse( )
print(x)

#tolist method:
#convert array into list
import array
x=array.array('i',[100,200,400,500,600,700])
list=x.tolist( )
print(list)

#typecode attribute/variable:
import array
x=array.array('i',[133,122,34,56])
print(x.typecode)

#itemsize attribute
import array
x=array.array('i',[133,122,34,56])
print(x.itemsize)

#sorting method

import array
x=array.array('i',[133,122,34,56])
y=sorted(x)
print(y)

#sorting method to print in decending order

import array
x=array.array('i',[133,122,34,56])
y=sorted(x,reverse=True)
print(y)
#another method
import array
x=array.array('i',[133,122,34,56])
y=sorted(x,reverse=False)
print(y)

#swap
#write a program to print sorting values to be swap

a=10
b=20

temp=a
a=b
b=temp
print('a=',a)
print('b=',b)





