"""
------------------------------------------------------------------------
CP164 Assignment 01, Task 09
------------------------------------------------------------------------
Author:  Name
ID:      ID
Email:   Email
__updated__ = "2022-05-15"
------------------------------------------------------------------------
"""

from functions import substitute

string  = 'David'
ciphertext = "DAVIBROWNZCEFGHJKLMPQSTUXY"

estring = substitute(string, ciphertext)

print(estring)


