"""
-------------------------------------------------------
Assignement 05 Task 02
-------------------------------------------------------
Author:  Name
ID:      ID
Email:   Email
__updated__ = "2023-06-12"
-------------------------------------------------------
"""
from Sorted_List_array import Sorted_List


lst = Sorted_List()


lst.insert(100)

lst.insert(200)

lst.insert(200)

lst.clean()


print()
print("Printing")
for value in lst:
    print(value)


print()
print("Printing")
print(100 in lst)


lst.insert(100)

print()
print("Printing")
print(lst.count(100))


print()
print("Printing")
print(lst.find(100))


print()
print("Printing")
print(lst[2])


print()
print("Printing")
print(lst.index(100))


lst2 = Sorted_List()

lst2.insert(100)

lst2.insert(1000)


lst3 = Sorted_List()

lst3.intersection(lst, lst2)

print()
print("Printing")
for value in lst3:
    print(value)
print()
print("Printing")
print(lst2.max())


print()
print("Printing")
print(lst2.min())


print()
print("Printing")
print(lst.peek())


lst2.remove(100)

print()
print("Printing")
for value in lst2:
    print(value)


lst.remove_front()

print()
print("Printing")
for value in lst:
    print(value)


lst4 = Sorted_List()

lst4.insert(11)

lst4.insert(22)

lst4.insert(22)

lst4.remove_many(22)

print()
print("Printing")
for value in lst4:
    print(value)


lst4.insert(1000)

lst4.insert(100)


target1, target2 = lst4.split()


print()
print("Printing")
for value in target1:
    print(value)

print()
print("Printing")
for value in target2:
    print(value)


target1.insert(1000)

target1.insert(100000)


target3, target4 = target1.split_alt()


print()
print("Printing")
for value in target3:
    print(value)


print()
print("Printing")
for value in target4:
    print(value)


target3.insert(100)

target3.insert(100000)


target5, target6 = target3.split_key(10000)


print()
print("Printing")
for value in target5:
    print(value)

print()
print("Printing")
for value in target6:
    print(value)


target3.union(target5, target6)

print()
print("Printing")
for value in target3:
    print(value)
