#python iterator
#return iterator from tuple and print each value

mytuple = ("apple","banana","cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))


#Strings are also iterable objects containing a sequence of characters

mystr = "banana"
myit= iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))


#looping through an iterator

#iterate the values of tuple

mytuple= ("apple","banana","cherry")

for x in mytuple:
    print(x)

#iterate the character of a string

mystr="banana"

for x in mystr:
    print(x)
    
