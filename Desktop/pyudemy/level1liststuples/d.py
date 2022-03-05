# Write a Python program that removes all occurrences of the element elem_to_remove from a list.
# The output of the program should be the new list with the element removed.
# If the element is not found in the list, print the message "Not Found".
# If the list is empty, print "Empty List".

# The list method .remove() only removes the first occurrence of an element in a list.
# The program must remove all occurrences of the element from the list.
# You can get the number of occurrences of an item with the .count() list method.

# List              Element to remove       Output
# [1,2,3,4]             [2]                 [1,3,4]
# [3,3,2,1]             [3]                 [2,1]
# ["a", "b", "c", "b"]  ["b"]               ["a", "c"]
# [3,4,5,6]             [7]                 "not found"
# []                     [0]                "list empty"

my_list = [3,3,2,1] # remove 3
elem_to_remove = 3

if not my_list:
    print("empty list")
elif my_list.count(elem_to_remove) == 0:
    print("not found")
else:
    for i in range(my_list.count(elem_to_remove)):
        my_list.remove(elem_to_remove)
    print(my_list)