"""
-------------------------------------------------------
Assignment 03 Task 01
-------------------------------------------------------
Author:  Name
ID:      ID
Email:   Email
__updated__ = "2023-05-30"
-------------------------------------------------------
"""

from Stack_array import Stack
from functions import *

source1 = Stack()
source2 = Stack()

source1.push(8)
source1.push(12)
source1.push(8)
source1.push(5)

source2.push(14)
source2.push(9)
source2.push(7)
source2.push(1)
source2.push(6)
source2.push(3)

target = (stack_combine(source1, source2))
for i in target:
    print(i)
