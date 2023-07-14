"""
-------------------------------------------------------
Lab 04 Task 03
-------------------------------------------------------
Author:  Ranjot Sandhu
ID:      169020301
Email:   sand0301@mylaurier.ca
__updated__ = "2023-06-06"
-------------------------------------------------------
"""

from List_array import List

list1 = List()

list1.append(100)

print(len(list1))

list1.insert(0, 200)

print(len(list1))

remove = list1.remove(200)

print(remove)