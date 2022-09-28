#Array
# write a program to read '10' integers in an array and find the count no.of even numbers and
#no.of odd numbers in an array?

import array
a= array.array('i',[ ])
n=int(input('enter the range of an array'))
for i in range(n):
    a.append(int(input('enter an array element..')))

evencount=0;oddcount=0        #2 ways :   ec=0;oc=0/ec=oc=0
for i in a:
    if i%2 ==0:
        evencount=evencount+1
    else:
        oddcount=oddcount+1
print('No.of even numbers=',evencount)
print('No.of odd numbers=',oddcount)
