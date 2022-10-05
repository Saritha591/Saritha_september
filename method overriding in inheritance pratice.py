#method overriding in inheritance:
#ex;1
class A:
    def display(self):
        print("method belongs to class A")
class B(A):
    def display(self):
        print("method belongs to class B")
        
b1= B( )
b1.display( )

#sample program with pass statement
class A:
    def display(self):
        print("method belongs to class A")
class B(A):
   pass  
b1= B( )
b1.display( )

#ex:2

class animal:
    def walk(self):
        print("hello, i am active animal")
class dog(animal):
    def walk(self):
        print("hello,i am active dog")

r=dog( )
r.walk( )

#ex:3

class Birds:
    def fly(self):
        print("hello, i am happy to fly")
class parrot(Birds):
    def fly(self):
        print("hello,i am happy to fly and i ate fruits ")

freedom=parrot( )
freedom.fly( )


