#oops pratice
#inheritance concept
#we can create a new class by using property of already existing class
#Inheritance new class are called as derived/child class
# and already existing class we called as base/parent class

class animal:
    def eating(self):
        print("eating")
class dog(animal):
    def bark(self):
        print("bark")

d=dog( )
d.eating( )
d.bark( )

#program

class polygon:
    def __init__(self,noofsides):
        self.n=noofsides
        self.sides=[o for i in range(noofsides)]
    def inputsides(self):
        self.sides=[float(input("enter sides"+str(i+1)+": "))for i in range(self.n)]
    def dissides(self):
        for i in range(self.n):
            print("sides",i+1,"is",self.sides(i))
class triangle(polygon):
    def __init__(self):
        polygon.__init__(self,3)
    def findarea(self):
        a,b,c=self.sides

s=(a+b+c)/2
area=(s*(s-a*(s-b)*(s-c)))
print('the area of triangle is %0.2f'%area)



# A Python program to demonstrate inheritance
 
# equivalent to "class Person(object)"
 
 
class Person(object):
                                       
    def __init__(self, name):
        self.name = name
                                       
    def getName(self):
        return self.name
                                    
    def isEmployee(self):
        return False
                                    
class Employee(Person):
                                          
    def isEmployee(self):
        return True
human=employee("saritha","true")
human.isemployee( )

                                        
