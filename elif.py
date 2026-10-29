"""
if condition1:
    block of code to be executed if condition 1 is true
elif condition2:
    block of code to be executed if condition 2 is true
else:
    block of code to be executed if all conditions are false
print grade depending on marks
90-100-A
80-90-B
70-60-C
50-60-D
rest-fail    
"""
marks=int(input("Enter marks to check grade: "))
if marks >=80 and marks <=100:
   print("Grade A")
elif marks>=70 and marks<=79:
   print("Grade B")
elif marks>=60  and marks<=69:
   print("Grade C")
elif marks>=50  and marks<=59:
   print("Grade D")
else:
   print("Fail")
#a program that asks user fro age and prints the age category
#<18-baby
#18-24-young adult
#24-45-adult
#45-65-mature adult
#>65-elderly
user_age=int(input("Enter your age: "))
if user_age < 18:
        print("baby")
elif 18 <= user_age <= 24:
        print("young adult")
elif 24 < user_age <= 45:
        print("adult")
elif 45 < user_age <= 65:
        print("mature adult")
else:
        print("elderly")
