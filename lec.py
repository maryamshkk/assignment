# tuple
# dictionaries
# list
students = [
    {
        "name" : "ali",
        "age"  : 20
    },
    {
        "name" : "maryam",
        "age"  : 21
    },
    {
        "name" : "tayaba",
        "age" : 18
    },
]
# for student in students:
#     if student["name"] == "maryam":
#         print(student["age"])
        
# print(students[2]["age"])
# teacher  = {
#     "name" : "maryam",
#     "age"  : 22,
#     "city" : "lahore"
# }
# print(teacher[age])

# test_list = [10,20,30] #mutable
# test_tuple = (40,50,60) #immutable 
# print(test_tuple[2])
# test_list.append(20)
# print(test_list)
# test_list.pop()
# print(test_list)
# test_list.insert(3,200)
# print(test_list)
# test_list.extend([12,13,14])
# print(test_list)
# print(test_list[2:])


names = ['alice', "bob", "charlie", "david"]

# create a new reversed list or reversed_names
# that contains elements in reverse order
# using slicing and print it

# reversed_names = names[::-1]
names.reverse()
# print(reversed_names)
print(names)
