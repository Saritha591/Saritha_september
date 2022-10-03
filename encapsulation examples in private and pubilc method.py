#Encapsulation in python
#oops
#private method example
class car:
    def __init__(self):
        self.__updatesoftware( )
    def drive(self):
        print("driving")
    def __updatesoftware(self):
        print("updating software")

blackcar=car( )
blackcar.drive( )




#public method

class animal:
    def __init__(self,name):
        self.name=name
class dog:
    def display(self):
        print(self.name)

d=dog("baby dog")
d.dog( )
