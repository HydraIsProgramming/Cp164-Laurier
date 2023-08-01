"""
-------------------------------------------------------
Assignment 04 Task 01
-------------------------------------------------------
Author:  Name
ID:      ID
Email:   Email
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
