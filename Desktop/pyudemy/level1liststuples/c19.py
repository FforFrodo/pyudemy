# Write a Python program that prints the largest and smallest values in a list
# Print the two values on the same line, separated by a space.
# The largest value should appear first and the smallest value should appear second.
# You may assume that the list only contains numeric values.
# If the list is empty, print None.
# Use min() max()

# List [3,4,5,6]    [-1,-2,-3,-4]   [0,0,0,0] []
# Output 6 3    -1 -4   0 0 []

# # My try
# my_list = [0,0,0,0]
# min = min(my_list)
# max = max(my_list)

# print(max, min)

# None gives error, use if else statement!

# solution

my_list = [3,4,5,6]

if my_list:
    print(max(my_list), min(my_list))
else:
    print(None)
