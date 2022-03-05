# Write a Python program that prints the elements of a list followed their corresponding indices.
# Each element and its index must be on the same line separated by a space.
# If the list is empty, print "Empty List".
# The enumerate() function can be used 
# to iterate over a counter and the elements of a sequence in parallel.

# List [1,2,3,4]
# Output 1 0 | 2 1 | 32 | 4 3
# List ["a", "b,", "c"]
# Output a 0 | b 1 | c 2
# List [] Output "Empty List"

# my try
# my_list = [1,2,3,4]

# if my_list:
#     for i in enumerate(my_list):
#         my_list[i]
#     print(my_list)
# else:
#     print("Empty List")

# Option 1

# my_list = ["a", "b", "c", "d"]

# if len(my_list) == 0:
#     print("empty list")
# else:
#     for i in range(len(my_list)):
#         print(my_list[i], i)

# my_list[i] = list with the element at i
# my_list[i], i = element at index and the index itself

# Option 2 solution!
my_list = [1,2,3,4]

if not my_list:
    print("list empty")
else:
    for i, elem in enumerate(my_list):
        print(elem, i)