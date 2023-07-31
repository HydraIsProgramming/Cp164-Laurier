"""
-------------------------------------------------------
Assignment 9 Task 1
-------------------------------------------------------
Author:  Ranjot Sandhu
ID:      169020301
Email:   sand0301@mylaurier.ca
__updated__ = "2023-07-18"
-------------------------------------------------------
"""
# Imports
from Hash_Set_array import Hash_Set
from functions import insert_words, comparison_total

hs = Hash_Set(20)

file = open('otoos610.txt', 'rt')

insert_words(file, hs)

file.close()

total, max_value = comparison_total(hs)

print("Using array-based list Hash_Set")
print()
print(f"Total Comparisons: {total:,}")
print(
    f"Word with maximum comparisons '{max_value.word}': {max_value.comparisons:,}")
