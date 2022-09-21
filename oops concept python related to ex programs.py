class Myclass:
    x=5

p1 = Myclass( )
print(p1.x)

class student:
    def display(self):
        print("hello")
student1= student( )
student1.display( )

#methods in class
class student:
    def __init__(self,name):
        self.name=name
        name="chandu"
        print(name)
    def display(self):
        print("hello",self.name)

student1= student("saritha")
student1.display( )
