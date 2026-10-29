#try and except is used for exception handling
"""
try:
      block of code that can cause an error
except:
      
"""
try:
     num=int(input("Enter a number: "))
     print(10/0)
except ZeroDivisionError:
     print("You cannot divide a number by zero")
#name error
try:
    print()
except NameError:
    print("The variable is not defined")
#try...except...else
#else block runs only if no exception occurs
#finally always runs with exeption or not
try:
    age=int(input("Enter your age:"))
except ValueError:
    print("Enter a numeric value")
else:
    print(f"Hey, you are {age} years old. ")
finally:
    print("This always runs")    

