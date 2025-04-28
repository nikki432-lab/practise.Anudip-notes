#strings in python(practise28/4/25)
#1. creating strings
#using single or double qoutes
string1 = 'Hello'
string2 = "Pyhton"
#using triple quotes for multiline string
''' This is a
multiline string.'''

#2. Acessing characters in string

text = "python"
print(text[0])
print(text[-1])

#3. String slicing

text = "Hello, Python!"
print(text[0:5])
print(text[:5])
print(text[7:])
print(text[-7:-1])

#4. Common string methods

#4.1 Changing case

text = "python Programming"
print(text.upper())
print(text.lower())
print(text.title())
print(text.capitalize())

#4.2 Chechking string properties

text = "Hello123"
print(text.isalpha())
print(text.isdigit())
print(text.isalnum())
print("   ".isspace())

#4.3 String Formatting
name = "Alice"
age = 25
print(f"My name is {name} and I am {age} years old.")

#4.4 String Replacement method(replace and split)

text = "i love python"
print(text.replace("love","like"))

text = "apple,orange,banana"
print(text.split(","))

#4.5 Removing Whitespaces

text = "    python   "
print(text.strip())
print(text.lstrip())
print(text.rstrip())

#5.String concatenation and Repetition
#concatenation
str1 = "Hello"
str2 = "World"
print(str1+" "+str2)

#Repetition
print(str1*3)

#6. Checking Substring

text = "Hello, Python!"
print("Python" in text)
print("java" not in text)
print("java" in text)

#7.Reverse a String

text = "python"
print(text[::-1])

#8. Iterating through a string

text = "python"
for char in text:
    print(char)

#9.Escape Characters

text = "Hello\nPython\tWorld"
print(text)


#

