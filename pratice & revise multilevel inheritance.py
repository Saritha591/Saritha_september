#multi level inheritance

class human:
    def display(self):
        print("hello,this is human class")
class employee(human):
    def work(self):
        print("hello,this is derived class employee")
class programmer(employee):
    def coding(self):
        print("hello,this is another derived class")
p1=programmer( )
p1.display( )
p1.work( )
p1.coding( )
