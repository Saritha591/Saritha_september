#write a program using range function
#first we will take input

lower_value = int(input("please enter the lowest range value:"))
upper_value = int(input("please enter the upper range value:"))

print("the prime numbers in range are:")
for number in range(lower_value,upper_value+1):
    if number > 1:
        for i in range(2,number):
            if(number%i)==0:
                break
            else:
                print(number)
