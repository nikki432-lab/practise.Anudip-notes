print("Hello World")

#declaring and initializing variables
name = "John"
age = 25
price = 99.9
is_active = True
print(name,age,price,is_active)

#name = input("Enter your name: ")
#print("Hello",name)

#conditional statements
# if statement
x = 10
if x>5:
    print("x is greater than 5")

#if else statement
    x = 3
    if x>5:
        print("x is greater than 5")
    else:
        print("x is not greater than 5")
        
#if-elif-else statement
        x = 10
        if x < 0:
            print("Negative number")
        elif x == 0:
            print("Zero")
        elif x>0 and x<=10:
            print("positive number but less than or equal to 10")
        else:
            print("x is greater than 10")

#Nested if statements

x = 15
if x > 10:
    print("above 20")
    if x > 20:
        print(" And also above 20")
    else:
        print("But not above 20")

#if statement with logical operators(and,or,not)

x = 7
y = 15
if x>5 and y>10:
    print("Both conditions are true")
if x>10 or y>10:
    print("Atleast one condition is true")
if not x > 10:
    print("x is not greater than 10")

#if statement with membership operators(in,not in)

fruits = ["apple","bannana","cherry"]
if "apple" in fruits:
    print("Apple is in the List")
if "grape" not in fruits:
    print("Grape is not in the List")

#for loop
#for loop through list

fruits = ["apple","banana","cherry"]
for fruit in fruits:
     print(fruit)

#Using range() in for loop
for i in range(5):
    print(i)

#Looping throigh a string

word = "python"
for letter in word:
    print(letter)

#While Loop
#using while loop
x = 1
while x <=5:
    print(x)
    x += 1
#1.break statement(loop control statements)(stops the loops immediately)
for i in range(10):
    if i == 5:
        break
    print(i)
#2.continue statement(skips the current iteration and moves to the next)
for i in range(5):
    if i == 2:
        continue
    print(i)

#3.elsse in loops(executes when loop completes normally)
for i in range(3):
    print(i)
else:
    print("Loop completed")

#4.pass statement(uses as placeholder,does nothing)

for i in range(3):
    if i == 1:
        pass
    print(i)

#functions in python
#1.Defining a function.

def greet():
    print("Hello, Welcome to the Python!")
greet()

#2.Functions with parameters
def add(a,b):
    return a + b
result = add(5,3)
print(result)

#3.default parameter values

def greet(name="Guest"):
    print(f"Hello, {name}!")
greet("Alice")
greet()

#4.Return statement

def square(num):
    return num*num
print(square(4))

#5.Variable length Arguments(*args and **kwargs)
#*args(NON-keyword arguments)
def sum_all(*numbers):
    return sum(numbers)
print(sum_all(1,2,3,4,5))

#**kwargs(Keyword arguments)
def person_info(**details):
    for key, value in details.items():
        print(f"{key}: {value}")
person_info(name="ALice", age =25, city="New York")

#6.Lambda Functions(Anonymous Functions)
square = lambda x: x*x
print(square(5))

add = lambda a,b: a+b
print(add(3,7))

#7.Recursive functions
#Factorial using Recursion

def factorial(n):
    if n==1:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(5))

#8.Functiuon Scope
#local and global variables
x = 10
def my_function():
    x = 5
    print("Inside function: ", x)

my_function()
print("Outside function: ", x)

#9.Higher Order Fyunctions
#Using map()
numbers = [1,2,3,4]
squared = list(map(lambda x: x**2, numbers))
print(squared)
 


    
    
 


         


