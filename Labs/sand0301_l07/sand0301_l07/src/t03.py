"""
-------------------------------------------------------
Lab 7 Task 3
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

target1, target2 = lst.split_alt_r()

print("Printing Target1: ")
for value in target1:
    print(value)

print()
print("Printing Target2: ")
for value in target2:
    print(value)
    
