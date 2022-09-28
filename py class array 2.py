#ARRAY
#how create an array & print an array using elements

import array
x=array.array('i',[10,29,30,46,37])
print(x)
print(type(x))



#creating an array using iterator "for loop"
import array
x=array.array('i',[10,29,30,46,37])
print(type(x))
for i in x:
    print(i,end=' ')

#Append menthod
#range( )
# creating an array up to 'n'elements using append method

import array
x=array.array('i',[ ])
n=int(input('Enter the range of an array....'))
for i in range(n):
    x.append(int(input('Enter an array elements...')))
for i in x:
   print(i,end=' ')

# creating an array using len( )             
import array
x=array.array('i',[ ])
n=int(input('Enter the range of an array....'))
for i in range(n):
    x.append(int(input('Enter an array elements...')))
for i in x:
   print(i,end=' ')
print('\n length of an array= ',len(x))

#Index value
#create an array

import array
x=array.array('i',[10,29,30,46,37])
print(type(x))
print(x[3])



