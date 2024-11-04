try:
    print(number)

except:
    print("An error has occurred!")


num1 = int((input("Enter an integer: ")))
num2 = 0
try:
    print(num1 / num2)

except:
    print("A ZeroDivisionError has occurred!")
finally:
    print("Success") #excecuted whether there is an error or not
