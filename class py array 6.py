#Array
#write a program to read 'n' integers in an array and read a search element
#and find the given search element found or not in an array?


import array
a= array.array('i',[ ])
n=int(input('enter the range of an array'))
for i in range(n):
    a.append(int(input('enter an array element..')))
b=int(input("enter the element to search:"))
for i in a:
      if i==b:
       print("search element found....")
       break
    
    

     
     # or
      
                 


a=int(input("enter size of array:"))
lst=[]
for i in range(a):
    b=int(input("enter element:"))
    lst.append(b)
print(lst)
c=int(input("enter the element to search:"))
for i in range(a):
    if lst[i]==c:
        print("element is",lst[i])
        print("at index",i)
        print("at position",i+1
