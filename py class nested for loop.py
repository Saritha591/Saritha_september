#nested for loop
#patterns

for i in range(1,6):
 for j in range(1,6):
     print(j,end='')
 print(" ",end='')

#patterns using this concept write a program to print right angle triangle using
#using nested for loop

rows = 5
# outer loop
for i in range(1, rows + 1):
    # inner loop
    for j in range(1, i + 1):
        print("*", end=" ")
    print('')

# write a program to print right angle traingle in a decrement using nested  for loop


rows = int(input("Inverted Right Triangle Numbers in Decreasing Ord Rows = "))

print("==Inverted Right Triangle of Numbers in Decreasing Order Pattern==")

for i in range(rows, 0, -1):
    for j in range(i, 0, -1):
        print(j, end = ' ')
    print()

# write a program to print  traingle/pyramid pattern in symbols  using nested  for loop

rows = int(input("Enter Pyramid Pattern Rows = "))

print("Pyramid Star Pattern") 

for i in range(0, rows):
    for j in range(0, rows - i - 1):
        print(end = ' ')
    for k in range(0, i + 1):
        print('*', end = ' ')

# write a program to print  traingle/pyramid  patterns in numbers using nested  for loop
n = int(input("Enter a number of n: "))
for i in range(n):    
    print(" "*(n-i-1),end="")    
    for j in range(i+1):        
        print(i+1,"",end="")    
    print()
    print()

# write a program to print  Dimond shape  patterns in numbers using nested for loop

n = int(input("Enter a number of n: "))
for i in range(n):    
    print(" "*(n-i-1),end="")    
    for j in range(i+1):        
        print("* ",end="")    
    print()
for i in range(n-1):    
    print(" "*(i+1),end="")    
    for j in range(n-i-1):        
         print("* ",end="")    
print()
   
