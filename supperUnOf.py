"""
Create a class Person with attributes name and age.
Then create a subclass Student that inherits from Person
and has an additional attribute student_id.
Implement a method in the Student class to display the student's details.
"""
class person():
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
        
class student(person):
    def __init__(self,name,age,idd):
        super().__init__(name,age)
        self.idd=idd
    def display(self):
        print(self.name,self.idd,self.age)
obj1=student("Bharat",19,"22JIO2301")
obj1.display()
        