"""
-------------------------------------------------------
Lab 02 Task 01
-------------------------------------------------------
Author:  Name
ID:      ID
Email:   Email
__updated__ = "2023-05-23"
-------------------------------------------------------
"""
from Stack_array import Stack

stack = Stack()

if stack.is_empty():
    print("Stack is empty")
else:
    print("Stack is not empty")

stack.push(1)

value = stack.pop()

print(f"{value} is no longer in the stack")

stack.push("bottom")

stack.push("top")

print(stack.peek())


