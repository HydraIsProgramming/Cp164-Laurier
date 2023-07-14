"""
-------------------------------------------------------
Lab 02 Task 05
-------------------------------------------------------
Author:  Ranjot Sandhu
ID:      169020301
Email:   sand0301@mylaurier.ca
__updated__ = "2023-05-23"
-------------------------------------------------------
"""
from Food_utilities import read_foods
from utilities import stack_test

file = open('food.txt', "rt")

foods = read_foods(file)

file.close()

stack_test(foods)

