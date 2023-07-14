"""
-------------------------------------------------------
Lab 03 Task 01
-------------------------------------------------------
Author:  Ranjot Sandhu
ID:      169020301
Email:   sand0301@mylaurier.ca
__updated__ = "2023-05-30"
-------------------------------------------------------
"""

from Queue_array import Queue

queue = Queue()

value = input("Enter a value: ")

queue.insert(value)

print(len(queue))
