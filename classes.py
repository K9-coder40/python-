#oop-Object Oriented Programming
      #ADVANTAGES
#.Provides a clear structure to programs
#.Makes code easier to maintain, reuse, and debug
#.Helps keep your code DRY (Don't Repeat Yourself)
#.Allows you to build reusable applications with less code
    #1.Define a class(blueprint)
class Student:
    #attributes-properties(name,age , height, course etc)
    #methods-display_details, display_email etc
    #constructor:runs automatically
    def __init__(self,name,age,course):
        self.name=name
        self.age=age
        self.course=course
    #method to show info
    def Info(self):
        return f"Student name is {self.name} and is {self.age} years old learning {self.course}"
    #2.Create an object
    #object is an instance of a class
st1 = Student("Mary", 20, "MIT")
st2 = Student("Wiliam",19,"Cybersecurity")
print(st1.name)
print(st1.age)
print(st1.course)
#calling the info() method
print(st1.Info())
print(st2.Info())

