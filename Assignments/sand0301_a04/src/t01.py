"""
-------------------------------------------------------
Assignment 04 Task 01
-------------------------------------------------------
Author:  Ranjot Sandhu
ID:      169020301
Email:   sand0301@mylaurier.ca
__updated__ = "2023-06-06"
-------------------------------------------------------
"""


from Queue_circular import Queue


target = Queue()
target.insert(1)
target.insert(2)
target.remove()

source = Queue()
source.insert(2)


equals = source == target 

print(equals)
