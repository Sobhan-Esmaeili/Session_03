
# Function Stages
# Function Definition --> def Function_Name():
# Function Call --> Function_Name()
# def calc():
#     x, y = 5, 10
#     print(x + y)
#
# calc()
#calc() # Will Run the Block of Code Within calc and Output 15


# Passing a Single Parameter
# Passing a Single Parameter Into a Function
# def PrintName(full_name):
#     print("Your Name is: {0}".format(full_name))
# PrintName("Sobhan Esmaeili")
# PrintName("Alireza Rostami")


# Multiple Parameters
# Passing Multiple Parameters Into a Function
# def Add_Nums(num_01, num_02):
#     result = num_01 + num_02
#     print("{0} + {1} = {2}".format(num_01, num_02, result))
# Add_Nums(5, 8) # Will output 13
# Add_Nums(3.5, 5.5) # Will output 9.0


# Passing a List
# Using a Function to Square All Information
# numbers_01 = [2, 4, 5, 10]
# numbers_02 = [1, 3, 6]
# def Squares(nums):
#     for num in nums:
#         print(num**2)
# Squares(numbers_01)
# Squares(numbers_02)


# Default Parameters
# Setting Default Parameter Values
# def calcArea(r, pi=3.14):
#     area = pi * (r**2)
#     print("Area: {0}".format(area))
# calcArea(2) # Assuming Radius is the Value of 2


# Making Parameters Optional
# Setting Default Parameter Values
# def PrintName(first, last, middle=""):
#     if middle:
#         print("{0} {1} {2}".format(first, middle, last))
#     else:
#         print("{0} {1}".format(first, last))
# PrintName("Sobhan", "Esmaeili")
# PrintName("Sobhan", "Esmaeili", "Tehrani") # Will Output With Middle Name


# Named Parameter Assignment
# Explicity Assigning Values to Parameters by Referencing the name
# def Add_Nums(num_01, num_02):
#     print(num_02)
#     print(num_01)
# Add_Nums(5, num_02 = 2.5)


# *args
# using args Parameter to Take in a Tuple of Arbitrary Values
# def OutPutData(name, *args):
#     print(type(args))
#     for arg in args:
#         print(arg)
# OutPutData("Sobhan Esmaeili", 5, True, "Alireza", 2.5)


# # Using Return
# # Using return keyword to return the Sum of two Numbers
# def add_Nums(num_01, num_02):
#     return num_01 + num_02
# result = add_Nums(5.5, 4.5) # Saves Returned Value Into result
# print(result)
# print(add_Nums(10, 10)) # Doesn't Save Returned Value


# # Ternary Operator
# # Shorthand Syntax Using a Ternary Operator
# def search_list(my_list, my_variable):
#     return True if "Sobhan" in my_list else False
# result = search_list(["Ali", "Mohammad", "Sobhan", "Reza"], 1) # result = True
# print(result)


# # Scope
# # Global Scope Access
# # Where Global Variables Can be Accessed
# number = 5
# def scope_test():
#     number += 1 # Not Accessible Due to Function Level Scope
# scope_test()

# # Handling Function Scope
# # Accessing Variables Defined in a Function
# def scope_test():
#     word = "Sobhan"
#     return word
# value = scope_test()
# print(value)


# # Declaring a Dictionary
# # Declaring a Dictionary Variable
# empty = {} # Empty Dictionary
# person = {"name": "Sobhan Esmaeili"} # Dictionary With One key/value Pair
# customer = {"name": "Sobhan", "age": 35} # Dictionary With two key/value Pairs
# print(customer)


# # Accessing Dictionary Information
# # Accessing Dictionary Information Through Keys
# person = {"name": "Sobhan"}
# print(person["name"]) # Access Information Through the Key


# # Using the Get Method
# # Using the get Method to Access Dictionary Information
# person = {"name": "Sobhan"}
# print(person.get("name")) # Retrieves Value of Name key as Before
# print(person.get("age")) # Retrieves Value of Name key as Before
# print(person.get("age", "35")) # get is a Secure Way to Retrieve Information

# # Dictionaries with Lists
# # Storing a list within a Dictionary and Accessing It
# data = {"sports": ["baseball", "football", "hockey", "soccer"]}
# print(data["sports"][0]) # First Access the key, then the index


# # Lists with Dictionaries
# # Storing a Dictionary Within a List and Accessing It
# data = ["Sobhan", "Ali", {"name": "Mehdi"}]
# #print(data[2]) # the Dictionary is in index 2
# print(data[2]["name"]) # First Access the Index, then Access the key


# # Dictionaries with Dictionaries
# # Storing a Dictionary within a Dictionary and Accessing It
# data = {"team": "Perspolis", "wins": {"2018": 108, "2017": 93}}
# #print(data["wins"]) # Will output the Dictionary Within the Wins key
# print(data["wins"]["2018"]) # First Access the Wins key, Then the Next key


# Adding New Information
# Adding New key/value Pairs to a Dictionary
# car = {"year": 2018}
# # print(car)
# car["color"] = "Blue"
# print("Year: {0} \t Color: {1}".format(car["year"], car["color"]))


# # Changing Information
# # Updating a value for a key/value pair that Already Exists
# car = {"year": 2018, "color": "Blue"}
# #print(car)
# car["color"] = "Red"
# print("Year: {0} \t Color: {1}".format(car["year"], car["color"]))


# # Deleting Information
# # Deleting a key/value pair from a dictionary
# car = {"year": 2018}
# try:
#     del car["year"]
#     print(car)
# except:
#     print("That key does not exist")


# Looping a Dictionary
# Looping Only Keys
# looping over a dictionary via the keys
# person = {"name": "Sobhan", "age": 35}
# for key in person.keys():
#     print(key)
# print(person[key]) # will output the value at the current key


# # Looping Only Values
# # looping over a dictionary via the values
# person = {"name": "Sobhan", "age": 35}
# for value in person.values():
#     print(value)


# # Looping Key-Value Pairs
# # looping over a dictionary via the key/value pair
# person = {"name": "Sobhan", "age": 35}
# for key, value in person.items():
#     print("{0}: {1}".format(key, value))