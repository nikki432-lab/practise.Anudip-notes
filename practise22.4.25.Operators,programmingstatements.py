#Operators
#1.Airthmetic Operators

a = 10
b = 5
print("addition",a+b)
print("subtraction",a-b)
print("Multiplication",a*b)
print("Division",a/b)
print("Modulus",a%b)
print("Floor Division",a//b)
print("Exponentiation",a**2)

#2.Assignment Operators

x =10
x+=5
print(x)

#3.Comparsion(relational)Operators

a = 10
b = 5
print(a>b)
print(a==b)
print(a!=b)
print(a<b)
print(a>=b)
print(a<=b)

#4.Logical operators
a = True
b = False
print(a and b)
print(a or b)
print(not a)

#5.Bitwise operators
a = 5
b = 3
print(a&b)
print(a|b)
print(a^b)
print(~a)
print(a<<1)
print(a>>1)

#6.Membership operators(in,not in)
my_list = [1,2,3,4,5]
my_string = "python"

print(3 in my_list)
print(6 not in my_list)
print("p" in my_string)
print("z" not in my_string)

print("                    ")

#Programming statements in python
#1.Expression statements
x = 5+3
print(x)

#2.Assignment statements
name =" Alice"
age = 25
pi = 3.14
print(name,age,pi)

#3.Condtional statements(Descision Making)

x = 10
if x>0:
    print("Positive number")
elif x<0:
    print("Negative number")
else:
    print("Zero")

#import math
import math
print(math.sqrt(16))

#4.Exception Handling Statements(used to handle errors)

#result = 10/0
#except ZeroDivisionEror:
#print("Cannot divide by zero")

#5.Pass,Break, and Continue Statements
#a).Pass statement
def my_function():
    pass

#b).Break statement

for i in range(5):
    if i==3:
        break
    print(i)

#c).Continue statement

for i in range(5):
    if i == 3:
        continue
    print(i)
    
#6. Return Statement

def square(num):
    return num*num
print(square(4))




