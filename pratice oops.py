#class creation ex:1
class person:
    pass
p=person( )
print(p)


#class creation ex:2

class student:
    def display(self):
     print("hi")
person1=student( )
person1.display( )


#class methods (display)
class myclass:
    def display(self):
        print("welcome to world")

members=myclass( )
members.display( )

#class methods (__init__)

class person:
    def __init__(self,name):
        self.name=name
    def display(self):
        print("hello",self.name)
human=person("saritha")
human.display( )
#using class methods write programs on it(program:1)
class myclass:
    def __init__(self,name):
        self.name=name
        name="saritha"
    def display(self):
        print("hii",self.name)
myclass1=myclass("chandu")
myclass1.display( )


#using class methods write programs on it(program:2)
class professor:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print("hello",self.name,self.age)
person1=professor("amul","30")
person1.display( )
#using class methods write programs on it(program:3)
#and using instance variables
class professor:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print("hello",self.name,self.age)
person1=professor("amul","30")
person1.display( )
print(person1.name)
print(person1.age)

#using class methods write programs on it(program:1)
#and using class variables and instance variables 
class student:
    clg="abc"           #class variable
    
    def __init__(self,rollno,name):
        self.name=name
        self.rollno=rollno

    def display(self):
        print("student name",self.name)
        print("student rollno",self.rollno)
        print("clg:",self.clg)
        
person1=student("saritha","12345")
person1.display( )

person2=student("chandu","12346")
person2.display( )

#using class methods write programs on it(program:2)
##and using class variables and instance variables

class person:
    def __init__(self,firstname,lastname):
        self.fname=firstname
        self.lname=lastname
    def display(self):
        print("firstname",self.fname)
        print("lastname",self.lname)
person1=person("saritha","katta")
person1.display( )

person2=person("teju","N")
person2.display( )

     
