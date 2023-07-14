"""
-------------------------------------------------------
Lab 03 Task 02
-------------------------------------------------------
Author:  Ranjot Sandhu
ID:      169020301
Email:   sand0301@mylaurier.ca
__updated__ = "2023-05-30"
-------------------------------------------------------
"""
from Queue_array import Queue

queue = Queue()

insert_value = input("Enter a value: ")

queue.insert(insert_value)

print(queue.peek())

value = queue.remove()

print(value)
