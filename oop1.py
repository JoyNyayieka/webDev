class Student:
    #Properties/ Variables/ Attributes/ Characteristics
    name = "Evans"
    gender = "Male"
    age = 23

    #Behaviours/ Method/ Function
    def study(self):
        print("Student is studying")

#Object1
student1 = Student() #Creating an object
student1.study()
print(student1.name)

#Object2
student2 = Student()