# A module is a file containing python code(functions,variables)
#built in modules e.g Math, Random,DateTime,os
import math
print(math.pi)
print(math.sqrt(49))
import os
print(os.getcwd())
#os.mkdir("Hello")
#print("Hello created successfully")
#help(os)
import random
#random num btwn 0-1
print(random.random())
print(random.randint(5,19))
import datetime
#print current date
print(datetime.date.today())
#print current date and time
print(datetime.datetime.now())
#check if a file exists
if os.path.exists("demo.txt"):
    print("file exists")
else:
    print("file does not exist")
