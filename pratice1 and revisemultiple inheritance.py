#multiple inheritance
#more one base class
#one derived class
#ex:1
class land_animal:
    def walk(self):
        print("this animal live in land")
class water_animal:
    def live(self):
        print("this animal live in water")
class DUCK(land_animal,water_animal):
    def display(self):
        print("this animal live in both land and water")
b1=DUCK( )
b1.display( )
b1.walk( )
b1.live( )


#ex:2

class Bus:
    def drive(self):
        print("bus is for people")
class car:
    def family(self):
        print("car is for small family")
class truck:
    def goods(self):
        print("truck for goods")
class train:
    def ways(self):
        print("tranfer people and goods from one place to another place")
class Transportation(Bus,car,truck,train):
    def carry(self):
        print("Transportation important in every day life")
w1=Transportation( )
w1.carry( )
w1.drive( )
w1.family( )
w1.goods( )
w1.ways( )



#ex:3

class calculation1:
    def summation(self,a,b):
        return a+b;
class calculation2:
    def multiplication(self,a,b):
        return a*b;
class Derived(calculation1,calculation2):
    def division(self,a,b):
        return a/b;
c1=Derived( )
print(c1.summation(40,30))
print(c1.multiplication(20,1))
print(c1.division(9,30))

class a:
    pass
a=a( )
d.update({a: "i an abject",a:"i am class"})



