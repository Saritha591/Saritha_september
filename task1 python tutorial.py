#lambda function
#1.it takes multiple arguments executes in a single line,In lamda dont have parenthesis
#2.multiple arguments we can pass in lamda,but we cannot do multiple operations


#ex:1
x=lambda y: y*2
print (x(7))

x = lambda y : y*2
print(x(7))
#complex operation in lambda
x=lambda y: y*2/5
print(x(7))
#multiple arguments passing in lambda function
x=lambda y,z: y*z*2
print(x(7,6))
#for normal function example
def a_name(x):
   return 2+2


##lambda function
#lambda x: x*2

#scalar values in lambda

(lambda x: x*5)(12)
list_1 = [1,2,3,4,5,6,7,8,9]
filter(lambda x: x%2==0, list_1


#Map function:
#map is used to map for list mapping of sequence
#map is used for mapping list

squares=list(map(lambda x: x**2,range(10)))
