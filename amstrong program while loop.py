#armstrong number for a given number using while loop

x=int(input("enter the number: "))
num = x
result=0
n=len(str(x))
while(x!=0):
    digit= x%10
    result = result + digit*n
    x= x//10
if num == result:
    print("given number is a  armstrong number")
else:
    print("given number is not armstrong number")
