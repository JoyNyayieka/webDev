
number =56 #Integer
second = 43.12 #Float
greeting = "Hello World" #String
isPythonInteresting = True #boolean

#Data Structures - Multiple values stored in a single variable
cars = ["toyota", "nissan", "vw"] #List - Ordered and changeable
fruits = ("banana", "orange", "apple") #Tuple - Ordered but unchangeable
countries = {"Kenya", "Tunisia", "Algeria"} #Set - unordered and unchangeable
student = {
    "firstname" : "Joy",
    "age" : 23,
    "course" : "Web Development",
    "nationality" : "Kenyan"
} #Dictionary - Key-value pair

print(cars)
print(fruits)
print(countries)
print(student)
print(student["course"])

print(number)
print(second)
print(isPythonInteresting)

#Determining a datatype
print(type(student))
print(type(countries))

#Typecasting- Converting one data type to another
print(float(number))
print(int(second))