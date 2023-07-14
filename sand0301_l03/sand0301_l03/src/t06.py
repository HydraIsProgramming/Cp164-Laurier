"""
-------------------------------------------------------
Lab 03 Task 06
-------------------------------------------------------
Author:  Ranjot Sandhu
ID:      169020301
Email:   sand0301@mylaurier.ca
__updated__ = "2023-05-30"
-------------------------------------------------------
"""
from Food_utilities import read_foods
from Priority_Queue_array import Priority_Queue
from utilities import array_to_pq, pq_to_array, priority_queue_test


pq = Priority_Queue()

source = [11, 22, 55, 44, 33]

array_to_pq(pq, source)

while len(pq) > 0:
    value = pq.remove()
    print(value)
    source.append(value)

array_to_pq(pq, source)

pq_to_array(pq, source)

print(source)

file_variable = open("foods.txt", "rt")

foods = read_foods(file_variable)

file_variable.close()

priority_queue_test(foods)
