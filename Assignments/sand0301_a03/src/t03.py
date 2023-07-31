"""
-------------------------------------------------------
Assignment 03 Task 03
-------------------------------------------------------
Author:  Ranjot Sandhu
ID:      169020301
Email:   sand0301@mylaurier.ca
__updated__ = "2023-05-30"
-------------------------------------------------------
"""
from Stack_array import Stack
from functions import stack_reverse

stack = Stack()

stack.push(5)
stack.push(4)
stack.push(3)
stack.push(2)
stack.push(1)

stack_reverse(stack)

for i in stack:
    print(i)