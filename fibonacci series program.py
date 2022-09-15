#write a program using fibnocci series
n=int(input("enter how many numbers you want in this series:"))
first = 0
secound = 1
for i in range(n):
    print(first)
    temp = first
    first = secound
    secound = temp+secound
