#list-used to store multiple items in a single variable
#lists are ordered ,allow duplicates and can be modified(mutable)
courses=["MIT","Cybersecurity","Data_Science","AGED"]
print(courses)
print(type(courses))
#accessing list item using index
print(courses[0])
print(courses[1])
#change item list
courses[1]="AGED"
print(courses)
#list methods append()
#append()-adds an element to the end of the list
courses.append("Kotlin")
print(courses)
courses.insert(2, "AI")
print(courses)
#sort()-alphabetically
courses.sort()
print(courses)
#len
print(len(courses))
#remove()-removes an item 
courses.remove("AGED")
#loop
for course in courses:
    print(course)