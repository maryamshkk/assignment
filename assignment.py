#VARIABLES & DATA TYPES

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
int_num = 12
float_num = 23.4
str_text = "i am she"

# Printing types
# Integer type
print(type(int_num))