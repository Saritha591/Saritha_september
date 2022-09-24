#for loop
#write a program to print tables using for loop format be like 1x9=9

'''s=int(input('enter table start number....'))
e=int(input('enter table end number....'))
t=int(input('enter table number....'))
for i in range(s,e):
    r=i*t
    print(i,'x',t,'=',r)'''

#table should be in proper format 9x1=9 using for loop
s=int(input('enter table start number....'))
e=int(input('enter table end number....'))
t=int(input('enter table number....'))
for i in range(s,e):
    r=i*t
    print(t,'x',i,'=',r)
