"""
-------------------------------------------------------
Lab 03 Task 04
-------------------------------------------------------
Author:  Name
ID:      ID
Email:   Email
__updated__ = "2023-05-30"
-------------------------------------------------------
"""
from Priority_Queue_array import Priority_Queue

pq = Priority_Queue()

value = int(input("Enter a number: "))

pq.insert(value)

print(pq.peek())
