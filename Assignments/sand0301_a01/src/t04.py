"""
------------------------------------------------------------------------
CP164 Assignment 01, Task 04
------------------------------------------------------------------------
Author:  Name
ID:      ID
Email:   Email
__updated__ = "2022-05-15"
------------------------------------------------------------------------
"""

from functions import is_palindrome

s = input("Enter word: ")

palindrome = is_palindrome(s)

if palindrome:
    print(f"{s} is a palindrome")
else:
    print(f'{s} is not a palindrome')
