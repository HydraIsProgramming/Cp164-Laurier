"""
------------------------------------------------------------------------
Assignment 8 Task 3
------------------------------------------------------------------------
Author:  Name
ID:      ID
Email:   Email
__updated__ = "2023-07-10"
------------------------------------------------------------------------
"""

from BST_linked import BST
from Letter import Letter
from functions import do_comparisons, letter_table

DATA = "ETAOINSHRDLUCMPFYWGBVKJXZQ"

bst = BST()

for value in DATA:
    letter = Letter(value)
    bst.insert(letter)

file = open('otoos610.txt', 'rt')

do_comparisons(file, bst)

file.close()

letter_table(bst)
