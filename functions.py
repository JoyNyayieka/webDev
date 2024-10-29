#Built-in functions

y =max(10,20,30,40)
print(y)

x = min(6,10, 17,30)
print(x)

z = pow(2, 3)
print("The result is ",z)

#User-defined functions
def greeting():
    print("Oyaore")

greeting() #Calling the function

def sum():
    a = int(input("Enter a number:"))
    b = int(input("Enter another number:"))
    print(a+b)

sum()

#Parameter/Variable and Argument/Value
def add(e , f):
    print(e + f)

add(4, 5)
add(36, 44)

def employee(fullname,age,position,degree):
    print(fullname,age,position,degree)

employee("John Doe", "25","Secretary","B.A")
employee("Jack Doe", "45","Accountant","BCom")
employee("Ben Doe", "28","H.R","B.A")
employee("Jane Doe", "30","I.T Support","I.T")