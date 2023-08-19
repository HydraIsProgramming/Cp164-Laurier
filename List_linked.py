"""
-------------------------------------------------------
Linked version of the list ADT.
-------------------------------------------------------
Author: Ranjot Sandhu
ID:     169020301
Email:  sand0301@mylaurier.ca
__updated__ = "2023-08-12"
-------------------------------------------------------
"""
# pylint: disable=W0212
# pylint: disable=E2515
# pylint: disable=E0303
# pylint: disable=W0613
# pylint: disable=E1128

# Imports
from copy import deepcopy


class List:
    """
    A linked List class.
    """

    def pair_count(self):
        """
        -------------------------------------------------------
        Returns the number of pairs of values (values that are adjacent
        to each other) in source.
        Use: source.pair_count(n)
        -------------------------------------------------------
        Returns‌​‌​​​​‌​​‌‌​​​​‌​‌‌‌​​​‌‌​‌:
            pairs - the number of pairs in source (int >= 0)
        -------------------------------------------------------
        """
        pairs = 0
        second = self._front
        first = self._front._next
        while first is not None and second is not None:
            if second._value == first._value:
                pairs += 1
            second = first
            first = first._next
        return pairs

    def rotate_front(self):
        """
        -------------------------------------------------------
        Moves the front node to the rear of the List.
        Use: source.rotate_front()
        -------------------------------------------------------
        Returns‌​‌​​​​‌​​‌‌​​​​‌​‌‌‌​​​‌‌​‌:
            None
        -------------------------------------------------------
        """
        if not self.is_empty():
            self._count -= 1
            x = self._front
            self._front = self._front._next
            a = self._front is None
            if a:
                self._rear = None
            b = self._rear is None
            if b:
                self._front = x
            else:
                self._rear._next = x
            x._next = None
            self._rear = x
            self._count += 1
        return

    def rotate_rear(self):
        """
        -------------------------------------------------------
        Moves the rear node to the front of the List.
        Use: source.rotate_rear()
        -------------------------------------------------------
        Returns‌​‌​​​​‌​​‌‌​​​​‌​‌‌‌​​​‌‌​‌:
            None
        -------------------------------------------------------
        """
        if self._front is not None and self._front is not self._rear:
            curr_node = self._front
            while curr_node._next is not self._rear:
                curr_node = curr_node._next
            self._rear._next = self._front
            self._front = self._rear
            self._rear = curr_node
            self._rear._next = None
        return

    def has_loop(self):
        """
        -------------------------------------------------------
        Determines if source contains a circular reference/loop.
        Use: loop = source.has_loop()
        -------------------------------------------------------
        Returns‌​‌​​​​‌​​‌‌​​​​‌​‌‌‌​​​‌‌​‌:
            loop - True if source contains a circular reference,
                False otherwise (bool)
        -------------------------------------------------------
        """
        if self._front is None:
            return False 
        a = self._front 
        b = self._front 
        while b is not None and b._next is not None:
            a = a._next
            b = b._next._next
            if a == b:
                return True
        return False

# DO NOT CHANGE CODE BELOW THIS LINE
# =======================================================================

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty list.
        Use: lst = List()
        -------------------------------------------------------
        Returns‌​‌​​​​‌​​‌‌​​​​‌​‌‌‌​​​‌‌​‌:
            a new List object (List)
        -------------------------------------------------------
        """
        self._front = None
        self._rear = None
        self._count = 0

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if the list is empty.
        Use: b = lst.is_empty()
        -------------------------------------------------------
        Returns‌​‌​​​​‌​​‌‌​​​​‌​‌‌‌​​​‌‌​‌:
            True if the list is empty, False otherwise.
        -------------------------------------------------------
        """
        return self._front is None

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the number of values in the list.
        Use: n = len(lst)
        -------------------------------------------------------
        Returns‌​‌​​​​‌​​‌‌​​​​‌​‌‌‌​​​‌‌​‌:
            the number of values in the list.
        -------------------------------------------------------
        """
        return self._count

    def append(self, value):
        """
        ---------------------------------------------------------
        Adds a copy of value to the end of the List.
        Use: lst.append(value)
        -------------------------------------------------------
        Parameters:
            value - a data element (?)
        Returns‌​‌​​​​‌​​‌‌​​​​‌​‌‌‌​​​‌‌​‌:
            None
        -------------------------------------------------------
        """
        # Create the new node.
        node = _List_Node(value, None)

        if self._front is None:
            # list is empty - update the front of the List.
            self._front = node
        else:
            self._rear._next = node
        # Update the rear of the List.
        self._rear = node
        self._count += 1
        return

    def __iter__(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through the list
        from front to rear.
        Use: for v in s:
        -------------------------------------------------------
        Returns‌​‌​​​​‌​​‌‌​​​​‌​‌‌‌​​​‌‌​‌:
            yields
            value - the next value in the list (?)
        -------------------------------------------------------
        """
        current = self._front

        while current is not None:
            yield current._value
            current = current._next


class _List_Node:
    """
    A linked List Node class.
    """

    def __init__(self, value, next_):
        """
        -------------------------------------------------------
        Initializes a list node that contains a copy of value
        and a link to the next node in the list.
        Use: node = _List_Node(value, _next)
        -------------------------------------------------------
        Parameters:
            _value - value value for node (?)
            _next - another list node (_List_Node)
        Returns‌​‌​​​​‌​​‌‌​​​​‌​‌‌‌​​​‌‌​‌:
            a new _List_Node object (_List_Node)
        -------------------------------------------------------
        """
        self._value = deepcopy(value)
        self._next = next_
