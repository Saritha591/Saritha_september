class student:
    clg='abc'    #class variable

    def __int__(self,rollno,name):
        self.rollno= rollno
        self.name= name
    def display(self):
        print("student name:",self.name)
        print("student rollnumber:",self.rollno)
        print("college:",student.clg)

student1= student('abc701',"Bujji")
Student1.display( )

student2= student('abc702',"chandu")
Student2.display( )

