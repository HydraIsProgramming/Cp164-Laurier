"""
-------------------------------------------------------
Lab 02 Task 03
-------------------------------------------------------
Author:  Name
ID:      ID
Email:   Email
__updated__ = "2023-05-23"
-------------------------------------------------------
"""
from Stack_array import Stack
from utilities import array_to_stack, stack_to_array

stack = Stack()

source = ["First","top", "middle", "bottom"]

array_to_stack(stack, source)

target = []

stack_to_array(stack, target)

print(target)

