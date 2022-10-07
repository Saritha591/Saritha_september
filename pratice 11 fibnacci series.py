#fibinacci series
n=int(input('enter the value of n'))
a=1
b=1
print(a)
print(b)
c=0
while c<n:
    c=a+b
    print(c,end=' ')
    a=b
    b=c
    
