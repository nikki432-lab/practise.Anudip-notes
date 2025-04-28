#Lists in Python
#1. Creating a list
#creating a list with different data types

my_list = [10, "python", 3.14, True]
print(my_list)

#2. Acessing Elements in a List(indexing)

fruits = ["apple", "banana", "cherry"]
print(fruits[0])
print(fruits[-1])

#3.Slicing a list
numbers = [10,20,30,40,50]

print(numbers[1:4])
print(numbers[:3])
print(numbers[2:])
print(numbers[::-1])

#4 Modifying a lsit

fruits =  [ "apple", "banana", "cherry"]
fruits[1]="orange"
print(fruits)

#5.Adding Elements to a list

#5.1 append()-Add an element to the end

fruits = ["apple","banana"]
fruits.append("cherry")
print(fruits)

#5.2 insert()-Insert at a specific position


fruits.insert(1,"mango")
print(fruits)

#5.3 extend()-Add mutiple elements

fruits.extend(["grape","kiwi"])
print(fruits)

#6.Removing elements from a list
#6.1. remove()- Remove a specifc element

fruits = ["apple","banana","cherry"]
fruits.remove("banana")
print(fruits)

#6.2 pop()-Remove an element by index

fruits = ["apple","banana","cherry"]
fruits.pop(1)
print(fruits)

#6.3 del - Delete an element or the entire list

fruits = ["apple","banana","cherry"]
del fruits[1]
print(fruits)

#6.4 clear()-Remove all elements

fruits = ["apple","banana","cherry"]
fruits.clear()
print(fruits)


#7. Looping through a list
#7.1 Using for loop

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

#7.2 Usine while Loop

fruits = ["apple","banana","cherry"]
i = 0
while i < len(fruits):
    print(fruits[i])
    i += 1

#7.3 USing list comprehension

fruits = ["apple","banana","cherry"]
[print(fruit) for fruit in fruits]

#8.Checking if an element exists

fruits = ["apple","banana","cherry"]
if "banana" in fruits:
    print("yes, banana is in the list")

#9.Sorting a list
#9.1 sort() - Sort in a ascending order

numbers = [5,2,8,1,9]
numbers.sort()
print(numbers)

#9.2 sort(reverse=True)-Sort in descending order

numbers.sort(reverse=True)
print(numbers)

#9.3 sorted()-Returns a new sorted list

sorted_numbers = sorted(numbers)
print(sorted_numbers)

#10.Copying a list
#10.1 Using copy()

fruits = ["apple","banana","cherry"]
new_fruits = fruits.copy()
print(new_fruits)

#10.2 Using list()

fruits = ["apple","banana","cherry"]
new_fruits = list(fruits)
print(new_fruits)

#11 List Comprehension
#11.1creating a list with squares of numbers 1 to 5

x = [1,2,3,4,5]
squares =  [x**2 for x in range(1,6)]

#11.2 Filtering Even numbers

numbers = [1,2,3,4,5,6]
even_numbers = [x for x in numbers if x%2==0]
print(even_numbers)

#12.Nested lists (lists withtin lists)

matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(matrix[1])
print(matrix[1][2])
print(squares)
 

