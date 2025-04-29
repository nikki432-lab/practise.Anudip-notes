#Tuples in python
#1.Creating a tuple

my_tuple = (10, "python", 3.14, True)
print(my_tuple)

#creating a tuple wihtout parentheses()

another_tuple = 1,2,3
print(another_tuple)

#single elemenrt tuple(comma is necessary)

single_tuple = (10,)
print(type(single_tuple))

#2.Accessing tuple elements(indexing)

fruits = ("apple","banana","cherry")
print(fruits[0])
print(fruits[-1])

#3.Slicing a tuple

numbers = (10,20,30,40,50)
print(numbers[1:4])
print(numbers[:3])
print(numbers[2:])
print(numbers[::-1])

#4.Tuple Immutability(tuples canaot be modified after creation)

#my_tuple = (1,2,3)
#my_tuple[0] = 5
#print(my_tuple)

#5.Concatenation and repetition
#Concatenation

tuple1=(1,2,3)
tuple2=(4,5,6)
result=tuple1+tuple2
print(result)

#Repetition

repeat_tuple = ("python ",)*3
print(repeat_tuple)

#6.Tuple unpacking

person = ("Alice", 25, 'Engineer')
name,age,profession = person
print(name)
print(age)
print(profession)

#7. Looping through a list

#7.1using for loop

colors = ("red",'green','blue')
for color in colors:
    print(color)

#7.2using While loop

fruits = ("apple", "banana", "cherry")
i = 0
while i < len(fruits):
    print(fruits[i])
    i += 1

#8.Checking if an element exists(in and not in)(if and else)

fruits = ("apple", "banana", "cherry")
if "banana" in fruits:
    print("Yes, this fruit is in the tuple")
else:
    print("No, this fruit is not in the tuple")

#9. Using list Comprehension

fruits = ("apple", "banana", "cherry")
[print(fruit)for fruit in fruits]

#10. Tuple Methods
#10.1 count()-count occurrences

numbers = (1,2,3,1,1,4)
print(numbers.count(1))

#10.2.index()-fidn an index of an element

numbers = (10,20,30,40)
print(numbers.index(30))

#11.Nested tuples(tuples wihtin tuples)

nested_tuples = (1,(2,3,),(4,5,6))
print(nested_tuples[1])
print(nested_tuples[1][0])

#12.Convertin between Tuples and lists
#12.1converet tuple to list

numbers = (1,2,3)
numbers_list = list(numbers)
print(numbers_list)

#12.3 convert list to tuple

list = [1,2,3]
numbers_tuples = tuple(list)
print(numbers_tuples)









