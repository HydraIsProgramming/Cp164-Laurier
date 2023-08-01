"""
-------------------------------------------------------
Functions
-------------------------------------------------------
Author:  Name
ID:      ID
Email:   Email
__updated__ = "2023-07-18"
-------------------------------------------------------
"""
from Word import Word


def insert_words(fv, hash_set):
    """
    -------------------------------------------------------
    Retrieves every Word in file_variable and inserts into
    a Hash_Set. Each Word object in hash_set contains the number
    of comparisons required to insert that Word object from
    file_variable into hash_set.
    Use: insert_words(file_variable, hash_set)
    -------------------------------------------------------
    Parameters:
        fv - the already open file containing data to evaluate (file)
        hash_set - the Hash_Set to insert the words into (Hash_Set)
    Returns:
        None
    -------------------------------------------------------
    """
    for i in fv:
        words = i.strip().split(' ')
        for v in words:
            if v.isalpha():
                v = Word(v.lower())
                hash_set.insert(v)
    return


def comparison_total(hash_set):
    """
    -------------------------------------------------------
    Sums the comparison values of all Word objects in hash_set.
    Use: total, max_word = comparison_total(hash_set)
    -------------------------------------------------------
    Parameters:
        hash_set - a hash set of Word objects (Hash_Set)
    Returns:
        total - the total of all comparison fields in the Hash_Set
            Word objects (int)
        max_word - the word having the most comparisons (Word)
    -------------------------------------------------------
    """
    total = 0
    max_word = Word('a')
    for i in hash_set:
        if i:
            total += i.comparisons
            if i.comparisons >= max_word.comparisons:
                max_word = i
    return total, max_word
