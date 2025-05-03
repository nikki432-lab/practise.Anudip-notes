             #Exception Handling in python

#1. Exception
"""Exception is a Error that occurs during program execution
disrupting the normal flow of instructions"""
#Zerodidivision Error
#Value Error
#INdex Error
#File not found Error

#2. Basic Exception Handling(try-except method)'

try:
    num = int(input("Enter a number: "))
    result = 10/num
    print("Result:", result)

except ZeroDivisionError:
    print("Error: Cannot divide by Zero!")
except ValueError:
    print("Error: Invalid input! Please enter a number.")


#3. Handling Multiple Exceptions(in single block)

try:
    num = int(input("Enter a number: "))
    result = 10/num
except(ZeroDivisionError,ValueError):
    print("Invalid input or Division by Zero!")


#4. Using else with try-except

try:
    num = int(input("Enter a number: "))
    result = 10/num
except ZeroDivisionError:
    print("Cannot divide by zero!")
except ValueError:
    print("Inavlid Input!")
else:
    print("Result:", result)


#5. Using finally Block

try:
    file = open("data.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("File not found")
finally:
    print("Cleaning up resources...")

#6.  Raising Exceptions(raise Statements)

age = int(input("Enter age: "))
if age < 18:
    raise ValueError("Age must be 18 or above")


#7. Custom Exception handling

class InvalidAgeError(Exception):
    pass

try:
    age = int(input("Enter age: "))
    if age < 18:
        raise InvalidAgeError("You must be 18 or older!")
except InvalidAgeError as e:
    print("Error:", e)


#8 Handling File Exceptions

try:
    with open("file.txt", "r") as file:
        data = file.read()
except FileNotFoundError:
    print("The file does not exist!")


    


    




