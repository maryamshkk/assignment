# Variables & Data Types

#  Declare three variables: an integer, a float, and a string. Print their types
num_int = 10        #int
num_float = 10.5    #float
text = 'hello im maryam' #string

# Number in int
print(type(num_int))
# Number in float
print(type(num_float))
# Number in text
print(type(text))   

# Convert a float num = 12.7 to an integer and a string. Print the results.
num = 12.7
# Change to int
num_int = int(num)
# Change to string
num_str = str(num)

# Results
print("Float Number in Integer: ", num_int)
print("Float Number in String: ", num_str)

# Convert x = '25' (a string) to an integer and a float. Print the results.
x = '25'
# Convert to integer
num_int = int(x)
# Convert to float
num_float = int(x)

# Print in integer
print("String to integer: ", num_int)
# Print in float
print("String in Float: ", num_float)

# Check the datatype and mutability of given variables: a=10, b='Hello', c=3.14, etc.
a = 10          # Integer (Immutable)
b = "Hello"     # String (Immutable)
c = 3.14        # Float (Immutable)
d = [1, 2, 3]   # List (Mutable)
e = (4, 5, 6)   # Tuple (Immutable)
f = {7, 8, 9}   # Set (Mutable)
g = {"name": "Alice", "age": 25}  # Dictionary (Mutable)
h = True        # Boolean (Immutable)

# Checking types
print(type(a))  # <class 'int'>
print(type(b))  # <class 'str'>
print(type(c))  # <class 'float'>
print(type(d))  # <class 'list'>
print(type(e))  # <class 'tuple'>
print(type(f))  # <class 'set'>
print(type(g))  # <class 'dict'>
print(type(h))  # <class 'bool'>

# Checking mutability
try:
    a += 5  # Integers are immutable
    print("Integer is immutable.")
except:
    print("Integer is mutable.")

try:
    d.append(4)  # Lists are mutable
    print("List is mutable.")
except:
    print("List is immutable.")

try:
    e[0] = 10  # Tuples are immutable
    print("Tuple is mutable.")
except:
    print("Tuple is immutable.")

# Create a dictionary with variable names as keys and values as different datatypes.

my_dict = {
    "a" : 12,                            #int
    "b" :  23.4,                         # float
    "c" :  "hello",                      # str
    "d" :  [1,2,3],                      # list
    "e" :  (2,3,4),                      # tuple
    "f" :  {"a":12, "b":23, "c":34 },    # dict
    "g" :  {5,6,7},                      # set
    "h" :  True,                         # bool
    "i" :  None,                         # none type
}

# print dictionary 
print(my_dict)



# LISTS

# Create a list of five fruits and print the second and last element.
fruits = ["apple", "mango", "peach", "pineapple", "grapes"]

# Second and last element
print(fruits[1])
print(fruits[-1])

# Add a fruit at the start and end of the list, then print it
fruits = ["apple", "mango", "peach", "pineapple", "grapes"]
# Add new fruit at first and last
fruits.insert(0, "strawberry")
fruits.append("bluberry")
# Print
print(fruits)

# Remove the third element from the list and print it.
fruits = ["apple", "mango", "peach", "pineapple", "grapes"]
# Remove element
removed_fruit = fruits.pop(3)
# print removed element
print("Removed element is: ", removed_fruit)

# Replace the second element in [10, 20, 30, 40, 50] with 25.
new_list = [10,20,30,40,50]
# replace element
new_list[1] = 25
# print 
print("Second element 20 is replaced with 25", new_list)

#  Concatenate two lists and print the result.
list1 = [1,2,3,4]
list2 = [5,6,7,8]

# Concatenation
combined_list = list1 + list2
# newlist
print(combined_list) 

# Extract elements from index 1 to 4 using slicing.
int_list = [10,20,30,40,50,60,70]
# from index 1 to 4 elements
print(int_list[1:5])

# Create a list with an integer, string, and float. Print each element's type.
new_list = [12, "penny", 12.5]

# elements type
for element in new_list:
    print(f"Elements: {element}", "Type: ", type(element))



# TUPLES

# Create a tuple with five city names and print first and last element.
city_names = ("Lahore", "Karachi", "Peshawar", "Islamabad", "Sindh")

# Frirst and last element
print("First element: ", city_names[0])
print("Last element: ", city_names[-1])

# Try modifying a tuple element. Explain the error,(if any).

new_tuple = (1,2,3,4)
# change element
new_tuple[1] = 25

# Error:
# 'tuple' object does not support item assignment

#  Convert (10, 20, 30, 40, 50) into a list, modify an element, and convert back
tuple1 = (10, 20, 30, 40, 50)
# tuple to list
converted_list = list(tuple1)
#print list
print(converted_list) 
# converted back
converted_list[2] = 90
print(converted_list)
# back to tuple
tuple2 = tuple(converted_list)
print(tuple2)

# Check if 'purple' exists in a tuple.
colors = ('Yellow', 'green', 'blue', 'red', 'purple', 'black')
# Check purple presence
if "purple" in colors:
    print("Purple is present")
else: 
    print("Purple is not present")
    
#   Unpack ('Alice', 25, 'Doctor') into separate variables and print them.
tuple1 = ('Alice', 25, 'Doctor')
# Printing details
print("Name: ", tuple1[0])
print("Age: ", tuple1[1])
print("Profession: ", tuple1[2])

# Count occurrences of 5 in (1, 5, 2, 5, 3, 5, 4, 5).

numbers =  (1, 5, 2, 5, 3, 5, 4, 5)
# occurance
count_5 = numbers.count(5)
# print
print("The number of 5 occurs", count_5, "in tuple. ")


#  DICTIONARIES

#  Store student info (name, age, grade) in a dictionary and print the grade.
student = {
    "name"  : "Alice",
    "age"   : " 20",
    "grade" : "A"
}
print("Grade: ",student["grade"])

#  Add a new key-value pair and print the updated dictionary.
student["school"] = "The Punjab School"
print("Updated Dictionary ", student)

#  Update the age in a student dictionary and print the result.
student["age"] = 12
print("After Age Update: ",student)

#  Create a phonebook dictionary and check if 'John' exists in it.
phonebook ={
    "alice" : "123-456-789",
    "bob"   : "987-654-321"
}
if "John" in phonebook:
    print("John is in the phonebook")
else: 
    print("John is not in the phonebook")
    
#  Remove a key from a dictionary and print the updated dictionary.
del student["school"]
print("Updated dictionary: ", student)

#  Convert a dictionary's keys into a list and print them.
key_list = list(student.keys())
print("List of Dictionary Keys: ", key_list)


# SETS

# Create a set with five unique numbers and print it.
numbers = { 10,20,30,40,50}
print("Set of numbers", numbers)

#  Add an element to a set and remove an element from it. Print the result.
numbers.add(89)
numbers.remove(20)
print("Updated numbers",numbers)

#  Create two sets and perform union, intersection, and difference operations.
set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8}

print("Union", set1 | set2)
print("Intersection", set1 & set2)
print("Difference", set1 - set2)

#  Convert a list with duplicate values into a set and print the unique elements.
num_list = [1,2,2,3,4,4,5,5,5]
unique_numbers = set(num_list)
print("Unique numbers: ", unique_numbers) 

#  Check if a given element exists in a set and print an appropriate message.
element = 3
if element in unique_numbers:
    print(f"{element} is presenet in the set")
else: 
    print(f"{element} is not presenet in the set")

#  Create a set of vowels and check if 'z' is present in the set or not.
vowels = {'a', 'e', 'i', 'o', 'u'}
if 'z' in vowels:
    print("Z is present in list")
else: 
    print("Z is not present in list")
#  Try adding a list as an element inside a set. What happens? Explain.
try: 
    sample_set = {1,2,3}
    sample_set.add([4,5])
except TypeError as e:
    print("Error", e)
    print('''Explanation: Lists are mutable (changeable), 
        and sets only allow immutable (unchangeable) elements.''')
    
#  Convert a set into a sorted list and print the result
sorted_list = sorted(numbers)
print("Sorted list from sets: ", sorted_list)