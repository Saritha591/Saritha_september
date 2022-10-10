#Data Structures:

#LISTS

#list operations/methods

list1=[123,345,567,678]
print(list1)

fruits=['apple','mango','grapes','banana']
print(fruits)
#replace
fruits[2]='berries'
print(fruits)

#inset
fruits.insert(1,'cherry')
print(fruits)

#sort

fruits.sort( )
print(fruits)

list1.sort( )
print(list1)


#delete

list2=[1,2,3,4,5]
print(list2)

'''del list2
print(list2)'''

#append
fruits.append('blue berries')
print(fruits)
#reverse
fruits.reverse( )
print(fruits)

#pop
fruits.pop( )
'banana'

#using list as stacks
#in list & stack work same 

list3=[1]
print(list3)
list3.append(3)
list3.append(4)
print(list3)

list3.pop( )
print(list3)



#using lists as queues
#we want to import
#we want to implement a queue
#import collection.deque

from collections import deque
queue = deque(['saritha','pooja','teju'])
queue.append('sailu')
queue.append('dhana')
print(queue)
queue.popleft( )
print(queue)


#list comprehensions

squares=[ ]
for x in range(10):
    squares.append(x**2)
    

print(squares)



#
'''squares=list1(map(lambda x: x**2,range(10)))
print(squares)

#
squares =[x**2 for x in range(10)]
print (squares)'''


##
[(x,y)for x in [1,2,3] for y in[3,4,5] if x != y]
[(1,3),(1,4),(2,3),(2,1),(2,4),(3,1),(3,4)]
combs =[ ]
for x in [1,2,3]:
    for y in[3,4,5]:
        if x != y:
            combs.append((x,y))
print(combs)


# nested list comprehensions

'''matrix=[
    [1,2,34],
    [5,6,7,8],
    [9,10,11,12],
]

[[row[i] for row in matrix] for i in range(4)]
[[1,5,9],[2,6,10],[3,7,11],[4,8,12]]
transposed=[]
for i in range(4):
    transposed.append([row[i]for row in matrix])

print(transposed)'''

#Tuples and sequences
t=12345, 54324,'hello'
t[0]
print(t)
#tuples are nested

u=t,(1,2,3,4,5)
print(u)

'''#tuples are immutable
t[0]=8888
ptint(t)'''

t=1,
print(t)
len(t)

x,y,z=t


#sets
basket={'apple','orange','apple','pear','orange'}
print(basket)
a= set('abracadabra')
b=set('alacazam')
print(a)
print(b)


#dictionaries
tel={'jack': 4098,'sape':4139}
tel['guido']=4534
print(tel)
del tel['sape']
print(tel)
tel['irv']=4321
print(tel)
list(tel)
print(tel)
















