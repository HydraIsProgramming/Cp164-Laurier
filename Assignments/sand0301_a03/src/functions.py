"""
-------------------------------------------------------
Assignment 03 Functions File
-------------------------------------------------------
Author:  Name
ID:      ID
Email:   Email
__updated__ = "2023-05-30"
-------------------------------------------------------
"""

from Stack_array import Stack
from enum import Enum

OPERATORS = "+-*/"

def stack_combine(source1, source2):
    """
    -------------------------------------------------------
    Combines two source stacks into a target stack.
    When finished, the contents of source1 and source2 are interlaced
    into target and source1 and source2 are empty.
    Use: target = stack_combine(source1, source2)
    -------------------------------------------------------
    Parameters:
        source1 - a stack (Stack)
        source2 - another stack (Stack)
    Returns:
        target - the contents of the source1 and source2
            are interlaced into target (Stack)
    -------------------------------------------------------
    """
    
    target = Stack()
        
    while (not source1.is_empty()) and (not source2.is_empty()):
        target.push(source1.pop())
        target.push(source2.pop())
    # If the stacks are not equal in length
    while not source1.is_empty():
        target.push(source1.pop())
    while not source2.is_empty():
        target.push(source2.pop())
        
    return target

def stack_reverse(source):
    """
    -------------------------------------------------------
    Reverses the contents of a stack.
    Use: stack_reverse(source)
    -------------------------------------------------------
    Parameters:
        source - a Stack (Stack)
    Returns:
        None
    -------------------------------------------------------
    """
    
    temp = []
    
    while not source.is_empty():
        temp.append(source.pop())
    while len(temp) > 0:
        source.push(temp.pop(0))
    return
def postfix(string):
    """
    -------------------------------------------------------
    Evaluates a postfix expression.
    Use: answer = postfix(string)
    -------------------------------------------------------
    Parameters:
        string - the postfix string to evaluate (str)
    Returns:
        answer - the result of evaluating string (float)
    -------------------------------------------------------
    """
    stack = Stack()
    elements = string.split()
    for x in elements:
        if x not in OPERATORS:
            stack.push(x)
        else:
            first = float(stack.pop())
            second = float(stack.pop())
            if x =="+":
                stack.push(second + first)
            elif x == "-":
                stack.push(second - first)
            elif x == "*":
                stack.push(second * first)
            else:
                stack.push(second / first)
    answer = float(stack.pop())
    return answer


def reroute(opstring, values_in):
    """
    -------------------------------------------------------
    Reroutes values in a list according to a operating string and
    returns a new list of values. values_in is unchanged.
    In opstring, 'S' means push onto stack,
    'X' means pop from stack into values_out.
    Use: values_out = reroute(opstring, values_in)
    -------------------------------------------------------
    Parameters:
        opstring - String containing only 'S' and 'X's (str)
        values_in - A valid list (list of ?)
    Returns:
        values_out - if opstring is valid then values_out contains a
            reordered version of values_in, otherwise returns
            None (list of ?)
    -------------------------------------------------------
    """
    values_out = []
    stack = Stack()
    
    for x in opstring:
        if x == "S":
            if (len(values_in) == 0):
                values_out = None
            else:
                stack.push(values_in.pop(0))
        else:
            if(stack.is_empty()):
                values_out = None
            else:
                values_out.append(stack.pop())
    
    return values_out

MIRRORED = Enum('MIRRORED',
                {'IS_MIRRORED': "is a mirror", 'TOO_MANY_LEFT': "too many characters in L",
                 'TOO_MANY_RIGHT': "too many characters in R", 'MISMATCHED': "L and R don't match",
                 'INVALID_CHAR': "invalid character", 'NOT_MIRRORED': "no mirror character"})

def is_mirror_stack(string, valid_chars, m):
    """
    -------------------------------------------------------
    Determines if string is a mirror of characters in valid_chars around the pivot m.
    A mirror is of the form LmR, where L is the reverse of R, and L and R
    contain only characters in valid_chars.
    Use: mirror = is_mirror_stack(string, valid_chars, m)
    -------------------------------------------------------
    Parameters:
        string - a string (str)
        valid_chars - a string of valid characters (str)
        m - the mirror pivot string (str - one character not in valid_chars)
    Returns:
        mirror - the state of the string (Enum MIRRORED)
    -------------------------------------------------------
    """
    assert m not in valid_chars, \
        f"cannot use '{m}' as the mirror character"
    
    stopper = True
    mirror = MIRRORED.IS_MIRRORED
    length = len(string)
    stack = Stack()
    index_m = 0
    left = 0
    right = 0
    index = 0
    while stopper and index < length and string[index] != m:

        if string[index] in valid_chars:
            stack.push(string[index])
            index += 1
        else:
            stopper = False
            mirror = MIRRORED.INVALID_CHAR
    if stopper == True:
        index_m = index
        left = len(string[:index_m])

        right = len(string[index_m + 1:])
        index += 1

    if m not in string:
        stopper = False
        mirror = MIRRORED.NOT_MIRRORED

    if mirror and left > right:
        stopper = False
        mirror = MIRRORED.TOO_MANY_LEFT
    elif mirror and stopper and left < right:
        stopper = False
        mirror = MIRRORED.TOO_MANY_RIGHT

    while stopper == True and index < length and not stack.is_empty():
        c = stack.pop()
        if string[index] != c:
            stopper = False
            mirror = MIRRORED.MISMATCHED
        else:
            index += 1

    return mirror, stopper
