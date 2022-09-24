#For loop
#write a program to print reverse/decrement loop using for loop

'''for i in range(50,0,-1):
    print(i)'''
    
s=int(input('enter the start value....'))
e=int(input('enter the end/final value....'))
st=int(input('enter step value....'))
for i in range(e,s,st):
    print(i)
