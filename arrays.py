courses = ["MIT","Datascience","Cybersecurity"]

#Accessing an element in array
print(courses[1])

#Looping through the array
for y in courses:
    print("Course is",y)

#Adding a new element
courses.append("Android Dvelopment")
print(courses)

#Deleting an element
courses.remove("MIT")
print(courses)