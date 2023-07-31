"""
------------------------------------------------------------------------
CP164 Assignment 01, Task 06
------------------------------------------------------------------------
Author:  Name
ID:      ID
Email:   Email
__updated__ = "2022-05-15"
------------------------------------------------------------------------
"""

from functions import matrix_stats

a = [[1, 2, 3], [100, -99, 10]]
print(a)

small, large, total, average = matrix_stats(a)

print(f'Smallest Value: {small}')
print(f"Largest Value: {large}")
print(f"Total: {total}")
print(f"Average: {average:.2f}")
