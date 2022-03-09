# Write a Python program that prints (as a list) the elements of listA 
# that are not in listB as a list.
# If the lists have the same elements, print an empty list.
# If listA is an empty list, print an empty list.

# List A    [1,2,3,4]   [1,2,3,4]   []
# List B    [1,2]       [1,2,3,4]   [1,2,3]
# Ouput     [3,4]       []          []

ListA = [1,2,3,4]
ListB = [1,2]
difference = []

for elem in ListA:
    if elem not in ListB:
        difference.append(elem)
        
print(difference)