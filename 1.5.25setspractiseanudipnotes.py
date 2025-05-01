# Sets in Python
#Creating a Set {} or set()

my_set = {1,2,3,4,5}
print(my_set)

#duplicates are automatically removed

my_set = {1,2,2,3,4,4,5}
print(my_set)

#to find type(class)

my_set = set()
print(type(my_set))

#2. Set Properties
#-Unordered
#-Unique Elements
#-Mutable
#-Unindexed

#3. Adding elements to a set

#3.1 add()-Add a single element

fruits = {"apple", "banana"}
fruits.add("cherry")
print(fruits)

#3.2 update()-Add multiple elements

fruits.update(["grape", "orange"])
print(fruits)

#4. Removing elements from a set

#4.1 remove()-Remove a specific element(raises error if not found)

fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")
print(fruits)

#4.2 discard() - Remove an element(no error if not found)

fruits.discard("mango")
print(fruits)

#4.3 pop()- Remove an random element(no indexing)

numbers = {1,2,3,4,5}
numbers.pop()
print(numbers)

#4.4 clear()-Remove all elements

fruits = {"apple", "cherry"}
fruits.clear()
print(fruits)

#5. Looping through a list

fruits = { "apple", "banana", "cherry"}
for fruit in fruits:
    print(fruit)

#6.Checking if an element exists

fruits = { "apple", "banana", "cherry"}
print("banana" in fruits)
print("mango" in fruits)

#7.Set operatrions (mathematical operations)

#7.1 union() - Combine two sets(removes dupliactes)

A = {1,2,3}
B = {3,4,5}
print(A.union(B))

#7.2 Intersection() - gives Common elements from two sets

A = {1,2,3}
B = {3,4,5}
print(A.intersection(B))

#7.3 difference() - Elements in A but not in B

A = {1,2,3}
B = {3,4,5}
print(A.difference(B))
print(B.difference(A))

#7.3 Symmetric_difference() - Elements in A or B but not both(removes common elements)

A = {1,2,3}
B = {3,4,5}
print(A.symmetric_difference(B))
print(B.symmetric_difference(A))

#8. Convertin between sets and other data types

#8.1 Convert list into set(remove duplicates)

numbers_list = [1,2,2,3,4,4,5]
numbers_set = set(numbers_list)
print(numbers_set)

#8.2 Convert set into list

numbers_set = {1,2,2,3,4,5}
numbers_list = list(numbers_set)
print(numbers_list)

#8.3 convert tuple into set

tuples = (1,2,2,3,4,5)
set_list = set(tuples)
print(set_list)

#8.4 convert set into tuples

sets = {1,2,2,3,4,4,5}
tuples = tuple(sets)
print(tuples)

#9. Removing duplicates from a list

names = ["Alice", "Bob", "Alice", "Charlie", "Bob"]
unique_names = set(names)
print(unique_names) 






