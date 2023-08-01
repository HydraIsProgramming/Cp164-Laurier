"""
-------------------------------------------------------
Assignment 9 Task 3
-------------------------------------------------------
Author:  Name
ID:      ID
Email:   Email
__updated__ = "2023-07-18"
-------------------------------------------------------
"""
# Imports
from Hash_Set_BST import Hash_Set
from functions import insert_words, comparison_total

hs = Hash_Set(20)

file = open('otoos610.txt', 'rt')

insert_words(file, hs)

file.close()

total, max_value = comparison_total(hs)

print("Using linked BST Hash_Set")
print()
print(f"Total Comparisons: {total:,}")
print(
    f"Word with maximum comparisons '{max_value.word}': {max_value.comparisons:,}")
