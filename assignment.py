#a function that calculates area of rectangle hint area 1*W
def Area_of_rectangle(length,width):
    return length * width
print("Area of rectangle (length=16,width=5):",Area_of_rectangle(16,5))
#a funtion that calculates area of a circle a=3.14*r*r
def Area_of_circle(radius):
    return 22/7*radius*radius
#calling function
print("Area of a circle(r=3):", Area_of_circle(3))
#function that checks if a number is even or odd hint num%2==0
def check_even_odd(num):
  if num % 2 == 0:
    return "Even"
  else:
   return "Odd"
num = int(input("Enter a number: "))
#calling function
print(check_even_odd(num))

#function that multiplies 3 numbers
def multiply_three_numbers(x, y, z):
   return x * y * z
#calling function
print("Multiply (2, 3, 4):", multiply_three_numbers(2, 3, 4))