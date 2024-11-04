class Person:
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age


    def movement(self):
        print("Person is walking")

person1 = Person("Evans", "Male", 20)
print(person1.name)

person2 = Person("Faith", "Female", 25)
print(person2.name)

person3 = Person("Gladys", "Nonbinary", 28)
print(person3.name)
