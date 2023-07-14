"""
-------------------------------------------------------
Lab 01 Task 07
-------------------------------------------------------
Author:  Ranjot Sandhu
ID:      169020301
Email:   sand0301@mylaurier.ca
__updated__ = "2023-05-15"
-------------------------------------------------------
"""

# Imports
from Food_utilities import read_foods, get_vegetarian
# Constants

with open("foods.txt", "r") as f:
    foods = read_foods(f)

veggies = get_vegetarian(foods)

print("Vegetarian Foods:")
for food in veggies:
    print(food.name)