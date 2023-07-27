"""
-------------------------------------------------------
Lab 7 Task 6
-------------------------------------------------------
Author:  Name
ID:      ID
Email:   Email
__updated__ = "2023-06-27"
-------------------------------------------------------
"""
from List_linked import List

lst = List()

array = [22, 44, 55, 55, 11]

for value in array:
    lst.append(value)

lst.reverse_r()

for value in lst:
    print(value)
