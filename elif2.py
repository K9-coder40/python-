#a program that asks user fro age and prints the age category
#<18-baby
#18-24-young adult
#24-45-adult
#45-65-mature adult
#>65-elderly
user_age=int(input("Enter your age: "))
if user_age < 18:
        print("Baby")
elif 18 <= user_age <= 24:
        print("Young adult")
elif 24 < user_age <= 45:
        print("Adult")
elif 45 < user_age <= 65:
        print("Mature adult")
else:
        print("Elderly")
