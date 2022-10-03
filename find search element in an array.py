#write a program to read n integers in an array and read a search element and find the
#given element is found or not in an array

import array
x=array('i',[])
n=int(input('enter range of an array ..'))
print( )
for i in rangeO(n):
    x.append(int(input('enter an array element...')))
    print( )
print('given array is...')
for i in x:
      print(i,end=' ')
print( )
se=int(input('enter search element..'))
flag = False
j=0
for i in x:
    if i==se:
    flag = True
    p=j+1
    j+=1
    print( )
    if flag:
        print('given element is found in index position',p)
    else:
        print('given element is not found')
