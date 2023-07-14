"""
-------------------------------------------------------
Lab 02 Task 05
-------------------------------------------------------
Author:  Name
ID:      ID
Email:   Email
__updated__ = "2023-05-23"
-------------------------------------------------------
"""
from Food_utilities import read_foods
from utilities import stack_test

file = open('food.txt', "rt")

foods = read_foods(file)

file.close()

stack_test(foods)

