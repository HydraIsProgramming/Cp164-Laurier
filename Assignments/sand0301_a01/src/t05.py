"""
------------------------------------------------------------------------
CP164 Assignment 01, Task 05
------------------------------------------------------------------------
Author:  Name
ID:      ID
Email:   Email
__updated__ = "2022-05-15"
------------------------------------------------------------------------
"""
from functions import max_diff

string_values = input('Enter values (seperated by a comma): ').split(',')

values = []

for i in string_values:
    values.append(int(i))

diff = max_diff(values)

print(f"Biggest Difference: {diff}")
