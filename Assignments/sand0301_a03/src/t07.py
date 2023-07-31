"""
-------------------------------------------------------
Assignment 03 Task 07
-------------------------------------------------------
Author:  Ranjot Sandhu
ID:      169020301
Email:   sand0301@mylaurier.ca
__updated__ = "2023-05-30"
-------------------------------------------------------
"""

from functions import is_mirror_stack

string = "abcmcba"
valid_chars = "abc"

m = "m"

value = is_mirror_stack(string, valid_chars, m)

print(value)