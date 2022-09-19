# program to calculate the average of 3 numbers
#here in program i use input( ) so i ask user to give input values
#position of parameter are matter not the name of paramete
def average(n1,n2,n3):
    return(n1+n2+n3)/3.0
print("welcome")
num1 = int(input( ))
num2 = int(input( ))
num3 = int(input( ))
result = average(num1,num2,num3)
print(result)


#key word arguments
def average(n1,n2,n3):
    return(n1+n2+n3)/3.0
print("welcome")
'''num1 = int(input( ))
num2 = int(input( ))
num3 = int(input( ))'''
result = average (n2=5,n3=1,n1=8)           #here directly give input( )
print(result)

