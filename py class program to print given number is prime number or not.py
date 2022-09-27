# write a program to give number is prime number or not

x= int(input("enter  the value = "))
if x >1:
    for i in range(2,x):
        if(x %1) == 0:
            print(x,"is not a prime number")
            break
    else:
        print(x,"is a prime number")
else:
    print(x,"is not a prime number")
