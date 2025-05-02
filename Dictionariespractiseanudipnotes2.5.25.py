                               #Dictionaires in Python
#1.Creating a dictionary(created with curly bracws{} with Key - Value pairs separated by colons:,
#a)Creating a dictionary
student = {
    "name": "John",
    "Age": 25,
    "course": "Python"
}
print(student)

#b) creating an empty dictionary

empty_dict = {}
print(type(empty_dict))

#c) Using dictionary dict() constructor also we can create dictionaries

person = dict(name = "Alice", age = 30, city = "New York")
print(person)

#2.Acessing Dictionary Values

#2.1 Using Keys

student = {
    "name": "John",
    "Age": 25,
    "course": "Python"
}
print(student["name"])
print(student["Age"])
#print(student["city"]), if a key does not exists, it raises a key error

#2.2 Using get() method (to avoid errors)

person = dict(name = "Alice", age = 30, city = "New York")
print(person.get("name"))
print(student.get("Age"))
print(student.get("City", "Not Found"))
print(person.get("city"))

#3. Modifying a Dictionary

#3.1 Adding a new Key-Value pair

student = {
    "name": "John",
    "Age": 25,
    "course": "Python"
}
student["Gender"] = "Male"
print(student)

#3.2 Updating an Existing key

student["Age"] = 26
print(student)

#3.2 Using update() method (Add or Update multiple keys)

student.update({"Age":27, "City":"New York"})
print(student)

#4. Removing elements from a dictionary

#4.1 Using pop() Method (Removes and Return a value)

student = {
    'name': 'John',
    'Age': 27,
    'course': 'Python',
    'Gender': 'Male',
    'City': 'New York'
}
Age = student.pop("Age")
print(Age)
print(student)

#4.2 Using del Statement

del student["Gender"]
print(student)

#4.3 USing popitem() (Removes last inserted key-value pair)

student.popitem()
print(student)

#4.4 Using clear() (removes all items)

student.clear()
print(student)

#5 Looping through a dictionary
#5.1 Looping through keys and values separately
student = {
    'name': 'John',
    'course': 'Python'
}
for keys in student:
    print(keys)
for value in student.values():
    print(value)

#5.2 Looping through a Key-Value pairs,

for key, value in student.items():
    print(f"{key}:{value}")

#6 Checking for a Key in a dictionary

student = {
    'name': 'John',
    'course': 'Python'
}
if "name"  in student:
    print("Key Exists")

#7 Dictionary Comprehension

squares = { x: x**2 for x in range (1,6)}
print(squares)

#8 Nested Dictionaries

students = {
    "student 1":{ "name":"Alice", "Age":22},
    "student 2":{ "name":"Bob", "Age":25}
}
print(students["student 1"][ "name"])
print(students["student 2"][ "Age"])

#9 Converting between dictionaries and other data types
#9.1 Converting dictionary keys into list
student = {
    'name': 'John',
    'course': 'Python'
}
keys_list = list(student.keys())
print(keys_list)

#9.2 Converting dictionary values into list

values_list = list(student.values())
print(values_list)

#9.3 Converting dictionaries into list of tuples

list_items = list(student.items())
print(list_items)

#9.4 Converting dictionary  into tuples

item_list = tuple(student.items())
print(item_list)

#9.5 converting list of tuples to dictionary

item_list = [('name', 'John'), ('course', 'Python')]
new_dict = dict(item_list)
print(new_dict)











