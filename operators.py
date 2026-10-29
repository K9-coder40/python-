#operators are used to perform operations on variable values
#arithmetic -+,*,/,-,%
#addition
x=40
y=60
sum=x+y
print("The sum of",x,"and",y, "is",sum)
#substraction
print(f"The difference between {y} and {x} is {y-x}")
#multiplication
print(f"The product of {x} and {y} is {x*y}")
#division
print(f"The division of {y} and {x} is {y/x}")
#modulas-remainder of division %
print(f"The remainder of division of {y} and {x} is {y%x}")
#exponent **
print(x**2)
#comparison operators - >, <, >=,<=,==,!=
#used to compare two values . return true or false
#greater than  >
print(f"is {x} greater than {y}:? {x>y}")
#less than
print(f"is {x} less than {y}:? {x<y}")
#greater than or equal to
print(f"is {x} greater than or equal to {y}:? {x>=y}")
#less than or equal to
print(f"is {x} less than or equal to {y}:? {x<=y}")
#equal to
print(x==y)
#not equal to
print(x!=y)
#logical operators-AND,OR,NOT
a=3
print(a<5 and a>1)
print(a>5 and a>1)
#or returns true
print(a>2 or a>5)
#not returns the reverse
print(not(a>5))
#Assignment Operators =,+=,-=,*=
b=34
print(b)
b+=4 #b=b+4
print(b)
b-=1 #b=b-1
print(b)