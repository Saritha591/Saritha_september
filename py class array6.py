#Array4
# write a program to print and find out count of
#no.of positive values and no.of negative value?

import array
a= array.array('i',[ ])
n=int(input('enter the range of an array'))
for i in range(n):
    a.append(int(input('enter an array element..')))

pc=0
nc=0            # here pc is considered as positive count ,nc is considered as negative ccount
for i in a:
    if (i > 0):
        pc=pc+1
    else:
        nc=nc+1
print('/n no.of positive values=',pc)
print('no.of negative values=',nc)
