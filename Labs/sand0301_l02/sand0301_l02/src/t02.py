"""
-------------------------------------------------------
Lab 02 Task 02
-------------------------------------------------------
Author:  Ranjot Sandhu
ID:      169020301
Email:   sand0301@mylaurier.ca
__updated__ = "2023-05-23"
-------------------------------------------------------
"""
from Stack_array import Stack
from utilities import array_to_stack

stack = Stack()

source = ["top", "middle", "bottom"]

array_to_stack(stack, source)

while not stack.is_empty():
    value = stack.pop()
    print(value)