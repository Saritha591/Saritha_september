# for loop
# write a program to print odd numbers using for loop
n=int(input('enter n value...'))
for i in range(1,n+2,2):
    print(i)

#write a program to print natural numbers up to n using for loop

n=int(input('enter n value...'))
for i in range(1,n+1):
    print(i)

#write a program to print even numbers upto 'n' using for loop

n=int(input('enter n value...'))
for i in range(2,n+2,2):
    print(i)

#write a program to print sum of natural numbers upto 'n' using for loop
sum=0
n=int(input("enter the value of n...."))
for i in range(1,n+1):
    sum=sum+i
    print(sum)
##write a program for factorial of given number up to 'n'
#using for loop
f=1
n=int(input("enter the value of n...."))
for i in range(1,n):
    f=f*i
    print('f=', f)
