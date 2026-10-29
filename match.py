"""
#match variable:
#case value1:
  #block of code is executed
"""
day=int(input("Enter day of the week to print day: "))
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("invalid day. enter num between 1-7")
    