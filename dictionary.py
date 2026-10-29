#stores data in key value pairs
#{}
student={
    "name":"Mary",
    "age":19,
    "course":"MIT"
}
print(student)
print(type(student))
#accessing values
print(student["name"])
print(student["age"])
print(student["course"])
#add key:value pair
student["Town"]="Nairobi"
print(student)
#change value
student["name"]="John"
print(student)
#keys()-returns all keys()
print(student.keys())
#values-(returns all values())
print(student.values())
#items()-returns key:value pairs
print(student.items())
#loop
for x,y in student.items():
    print(x,":",y)