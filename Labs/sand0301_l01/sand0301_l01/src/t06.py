"""
-------------------------------------------------------
Lab 01 Task 06
-------------------------------------------------------
Author:  Name
ID:      ID
Email:   Email
__updated__ = "2023-05-15"
-------------------------------------------------------
"""

from Food_utilities import write_foods
from Food import Food
fv = open("new_foods.txt", "w")

k = Food("Milk", 2, False, 130)
y = Food("Sandwich", 0, True, 500)

l = [k, y]
write_foods(fv, l)
fv.close()

