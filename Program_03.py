
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