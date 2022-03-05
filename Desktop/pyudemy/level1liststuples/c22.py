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

# mytry
# my_list = [1,2,3,4]
# elem_to_remove = 2

# if not my_list:
#     print("list empty")
# else:
#     for i, elem_to_remove in enumerate(my_list):
#         i.remove(my_list)
#     print(my_list)
# fail, but i was aware there needed to be elif

my_list = [3,3,2,4]
elem_to_remove = 3

if not my_list:
    print("empty list")
elif my_list.count(elem_to_remove) == 0: # count list for (elemtoremove)
    print("not found")
else:
    for i in range(my_list.count(elem_to_remove)): # iterate list with count method
        my_list.remove(elem_to_remove) # remove (elemtoremove) at each iteration of range

print(my_list)

# if not my_list = false so print emptylist
# elif my_list.count(elemtoremove) == 0 <- counts elements in list containing .count()
# if ==0 then print not found as none were found in the list.

# [3,3,2,4]
# 1st iteration [3,2,4] .remove(3)
# 2nd iteration [2,4]   .remove(3)
# complete and print