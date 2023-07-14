"""
-------------------------------------------------------
Lab 4 Task 7
-------------------------------------------------------
Author:  Ranjot Sandhu
ID:      169020301
Email:   sand0301@mylaurier.ca
__updated__ = "2023-06-06"
-------------------------------------------------------
"""
from Food_utilities import read_foods
from utilities import list_test

file = open("food.txt", "rt")

source = read_foods(file)

file.close()

list_test(source)

