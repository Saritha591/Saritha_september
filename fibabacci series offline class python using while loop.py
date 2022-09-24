# Fibonacci series
# write a program to print fibonacci series up to 'n' using while loop
# Fibonacci series be like(1 1 2 3 5 13 21 34 55 89 144.....n)

'''a=1
b=1
print(a)
print(b)
c=0
while c<=50:
    c=a+b
    print(c)
    a=b
    b=c'''

# write a program to print fibonacci series upto 'n' using while loop
'''n=int(input("enter the number for fibonacci series ...."))
a=1
b=1
print(a)
print(b)
c=0
while c<=n:
    c=a+b
    print(c)
    a=b
    b=c'''


# when want to have only up to fibonacci number we use if condition with break statement   
a=1
b=1
print(a)
print(b)
c=0
while c<=100:
    c=a+b
    if c>100:
        break
    else:
        print(c)
        a=b
        b=c
    
