#python Inheritance
#create a parent class
class student:
    def __init__(self,fname,lname):
        self.firstname= fname
        self.lastname= lname

    def printname(self):
        print(self.firstname,self.lastname)

# use the person class to create an object and then execute the printname method

x= student("saritha","chandu")
x.printname( )


#create a child class
#Use the Student class to create an object, and then execute the printname method:

x= student("rani","raju")
x.printname( )

#Add the __init__( ) Function

class student(student):
    def __init__(self,fname,lname):
        self.fname= fname
        self. lastname= lname

    def printname(self):
        print(self.firstname,self.lastname)

class student(members):
    def __init__(self,fname,lname):
        people.__init__(self,fname,lname)

x= student("saritha","chandu")
x.printname( )

    
