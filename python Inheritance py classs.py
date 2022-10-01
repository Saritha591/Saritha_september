#python Inheritance

class birds:
    def eating(self):
        print("eating")

class parrot(birds):
    def flying(self):
        print("flying")

d=parrot( )
d.eating( )
d.flying( )


#base class and it include derived class(single inheritance)

class animal:
    def __init__(self,name):
        self.name=name                #initailization method

class dog(animal):
    def display(self):                #display method
        print(self.name)
d= dog("babydog")
d.display( )


#multiple and multilevel inheritance
#base class it includes multiple derived class(multiple inheritance)


#base class
class person:
    def display(self):
        print("hello,this is class person")

#derived class 1
        class employee(person):
            def printing(self):
                print("hello,this is derived class employee")

#derived class2
                class programmer(employee):
                    def show(self):
                        print("hello,this is another derived class programmer")
p1=programer( )
p1.display( )
p1.printing( )
p1.show( )
