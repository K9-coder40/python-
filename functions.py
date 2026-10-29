#function is a block of code that does a specific task
#def functionname()
     #body of the function
#function only runs when called
#functioname()
def greet():
    print("Hello Good evening!!!")
#calling the fucntion
greet()
greet()
#functions with parameter
def hello(first_name):
    print("Hey",first_name)
#calling the function
hello("Job")
hello("Jackline")
#function with multiple parameters
def display_details(name,age,course="MIT"):
    print(f"my name is {name} and I am {age} years old and I am studying {course}")
#calling function
display_details("Cate",19)
display_details("Mark",20,"Cybersecurity")
#a function that calculates area of rectangle hint area 1*W
#a funtion that calculates area of a circle a=3.14*r*r
#function that checks if a number is even or odd hint num%2==0
#function that multiplies 3 numbers
#lambda
#function that has a return keyword-returns a value when called
#function that adds two numbers and returns the sum
def addTwoNumbers(a,b):
    sum=a+b
    return sum
#calling the function
print(addTwoNumbers(30,40))
print(addTwoNumbers(56,22))
#calling the function and store the returned value in a variable
result=addTwoNumbers(30,65)
print("The sum is:",result)
#lambda function/anonymous function
#lambda argurments:expression
multiply=lambda a,b,c:a*b*c
print(multiply(33,4,6))
print(multiply(1,4,5))