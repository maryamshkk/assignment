# = assignment operator
# == equality operator
#  !=  no equal to 
#  < less than  
#  > greater than 
#  <= less than or equal to
#  >= greater than or equal to 
#  if condition 

# input character 
# marks: str = input()
# print("your marks are: ", marks ) 
# print("your marks are: ", type(marks)) 

# typecasting 
marks_string = "45"

marks_int = int(marks_string)

print("your marks are: ", type(marks_string))
print("your marks are: ", type(marks_int))

# function remainder, multiple, division,
def remainder(a,b):
    remainder = a % b
    
    print(remainder)

def division(a,b):
    division = a / b
    print(division)
    
def multiplication(a,b):
    multiplication = a * b
    print(multiplication)

remainder(4,5)
division(8,9)
multiplication(7,6)
    
    
# function
# dynamic function
def add_dynamic(m,n):
    sum_result= m + n
    
    print(sum_result)
    
add_dynamic(2,3)
add_dynamic(4,5)

# statis_function
def sum():
    m = 5
    n = 8
    
    sum_result = m+n 
    print(sum_result)
    
sum()

# even or odd
user_input = int(input("Enter a number: "))
if(user_input % 2 == 0):
    print("Even")
else: 
    print("Odd")



#
user_input= int(input("Enter a number : " ))
print("U entered: ", user_input)

if user_input > 0:
    print("Positive")
else: 
    print("Negative")