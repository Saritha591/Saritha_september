#polymorphism in python
#polymorphism in addition operator

num1 = 1
num2 = 2
print(num1+num2)

#polymorphism in string data type

str1 = " python"
str2 = "programing"
print(str1+" "+str2)

#functions polymorphism in python
print(len("saritha"))
print(len(["python","java","c"]))
print(len({"name":"shiva","address":"palakol"}))

#polymorphism in class methods

class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am a cat. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        print("Meow")


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am a dog. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        print("Bark")


cat1 = Cat("Kitty", 2.5)
dog1 = Dog("Fluffy", 4)

for animal in (cat1, dog1):
    animal.make_sound()
    animal.info()
    animal.make_sound()



#The len() method treats an object as per its class type.

students = ['Emma', 'Jessa', 'Kelly']
school = 'ABC School'

# calculate count
print(len(students))
print(len(school))

              
