"""
if condition:
    # block of code to execute if
    # condition is true
"""
x=1
if x>2:
    print(f"{x}) is greater than 2")
    print("code outside the if block")
"""
if . .else
if condition:
    #block of code to execute if condition is true
else:
    #block of code to execute if condition is true
"""

#a program that checks if a user can vote age>=18
age=12
if age>=18:
    print("you can vote")
else:
    print("you are not eligible to vote")
#ask user for their age and determine if they can drive(age>=18)
user_age=int(input("enter your age to determine if you can drive :"))
if user_age>=18:
    print("you can drive")
else:
    print("you are cannot drive")
