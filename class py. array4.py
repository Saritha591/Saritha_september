#write a program to print sum of elements in an array


import array
a= array.array('i',[ ])
n=int(input('enter the range of an array'))
for i in range(n):
    a.append(int(input('enter an array element..')))
sum=0
for i in a:
    sum=sum+i
print('sum=',sum)


#write a program to print biggest element in an array
import array
a= array.array('i',[ ])
n=int(input('enter the range of an array'))
for i in range(n):
    a.append(int(input('enter an array element..')))

bigvalue=0
for i in a:
    if i > bigvalue:
        bigvalue=i
print('biggest value=',bigvalue)


#write a program to print smallest element in an array

import array
a= array.array('i',[ ])
n=int(input('enter the range of an array'))
for i in range(n):
    a.append(int(input('enter an array element..')))

small=99999
for i in a:
    if i < small:
        small=i
print('smallest value=',small)
