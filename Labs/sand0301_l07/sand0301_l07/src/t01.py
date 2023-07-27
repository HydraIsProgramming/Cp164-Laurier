"""
-------------------------------------------------------
Lab 7 Task 1
-------------------------------------------------------
Author:  Name
ID:      ID
Email:   Email
__updated__ = "2023-06-27"
-------------------------------------------------------
"""
from List_linked import List

lst = List()

array = [22, 44, 33, 55, 11]

for value in array:
    lst.append(value)

p, c, i = lst._linear_search_r(33)

print(p._value)
print(c._value)
print(i)
