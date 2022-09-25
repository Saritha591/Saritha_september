#nested loop
#patterns using this concept write a program to print right angle triangle using numbers

i=0
while i<10:
    i+=1
    j=0
    while j<i:
        j+=1
        print(j,end=' ')
    print( )
# using patterns print reverse of right  angle traingle using nested loop
i=10
while i>=1:
    i-=1
    j=0
    while j<=i:
        j+=1
        print(j,end=' ')
    print( )

# write a program to print right angle traingle in a decrement using nested loop
i=10
while i>=1:
    i-=1
    j=10
    while j>i:
        print(j,end= ' ')
        j=j-1
    print( )
#write  a program to print right angle traingle with symbols
#symbol  using *

i=0
while i<5:
    i+=1
    j=0
    while j<i:
        j+=1
        print("*",end=' ')
    print( )




i=0
n=int(input('enter the n row symbol....'))
while i<n:
    i+=n
    j=0
    while j<i:
        j+=1
        print("*",end=' ')
    print( )

n=int(input('enter the n row symbol....'))
i=0
while i<n:
    i+=1
    j=0
    while j<i:
        j+=1
        print("*",end=' ')
    print( )


