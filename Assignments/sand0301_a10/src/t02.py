"""
-------------------------------------------------------
Assignment 10 Task 2
-------------------------------------------------------
Author:  Ranjot Sandhu
ID:      169020301
Email:   sand0301@mylaurier.ca
__updated__ = "2023-07-25"
-------------------------------------------------------
"""
# Imports
from List_linked import List
from Sorts_List_linked import Sorts
# Constants

array = [3153, 15, 3, 2441, 3282, 9178, 8932, 9385, 1213, 5880, 7239, 5821, 5087, 6889, 5288, 3969, 1951, 8010,
         3859, 5762, 6928, 1547, 3436, 490, 4063, 2980, 5929, 5369, 8998, 9710, 7916, 6949, 1657, 2766, 2046, 7739]

a = List()

for value in array:
    a.append(value)

Sorts.radix_sort(a)

for value in a:
    print(value, end=", ")