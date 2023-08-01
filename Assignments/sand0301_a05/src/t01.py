"""
-------------------------------------------------------
Assignement 05 Task 01
-------------------------------------------------------
Author:  Name
ID:      ID
Email:   Email
__updated__ = "2023-06-12"
-------------------------------------------------------
"""
from Food import Food
from Food_utilities import read_food, read_foods
from List_array import List
from utilities import array_to_list


file = open("food.txt", "rt")

foods = read_foods(file)

file.close()

lst = List()

array_to_list(lst, foods)

lasgna = Food("Lasagna", 7, False, 135)

lst.append(lasgna)

print("Printing...")
for value in lst:
    print(f"{value.name} = {lst.count(value)}")


lst.clean()

print()
print("Printing...")
for value in lst:
    print(f"{value.name} = {lst.count(value)}")

temp = [
    read_food("Gulab Jamun|2|True|300"),
    read_food("Burrito|4|False|200")
]


lst2 = List()

lst2.append(temp[0])

lst2.append(temp[1])

lst3 = List()

lst3.combine(lst, lst2)

print()
print("Printing...")
for value in lst3:
    print(f"{value.name}")

print()
print("Printing...")
print(lst3[10])


lst2.append(temp[0])

lst2.append(temp[1])


lst4 = List()

lst4.intersection(lst2, lst3)

print()
print("Printing...")
for value in lst4:
    print(f"{value.name}")


lst4.prepend(temp[0])

print()
print("Printing...")
for value in lst4:
    print(f"{value.name}")


lst4.remove_front()


print()
print("Printing...")
for value in lst4:
    print(f"{value.name}")


lst4.append(temp[0])

lst4.remove_many(temp[0])


print()
print("Printing...")
for value in lst4:
    print(f"{value.name}")


target1, target2 = lst3.split()

print()
print("Printing...")
for value in target1:
    print(f"{value.name}")

print()
print("Printing...")
for value in target2:
    print(f"{value.name}")


target3, target4 = target1.split_alt()

print()
print("Printing...")
for value in target3:
    print(f"{value.name}")

print()
print("Printing...")
for value in target4:
    print(f"{value.name}")


lst3.union(target3, target4)


print()
print("Printing...")
for value in lst3:
    print(f"{value.name}")
