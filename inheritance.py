#Parent class
class Animal:
    def breathe(self):
        print("Animal is breathing")

#Child class
class Dog(Animal):
    def bark(self):
        print("Dog is barking")


objectA = Animal()
objectD = Dog()
objectD.breathe()