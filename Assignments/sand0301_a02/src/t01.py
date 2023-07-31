"""
------------------------------------------------------------------------
CP164 Assignment 01, Task 01
------------------------------------------------------------------------
Author:  Ranjot Sandhu
ID:      169020301
Email:   sand0301@mylaurier.ca
__updated__ = "2022-05-23"
------------------------------------------------------------------------
"""
from Food import Food
from Food_utilities import read_foods, by_origin

file = open('food.txt', "rt")

foods = read_foods(file)

file.close()

origin = int(input(f"Enter a origin as an int\n{Food.origins()}: "))

origins = by_origin(foods, origin)

for food in origins:
    print(food, end="\n\n")