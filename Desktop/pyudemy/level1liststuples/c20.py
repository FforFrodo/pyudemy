# Write a Python program that checks if a list is empty or not.
# If the list is empty, print "Empty". Else, print "Not Empty".
# The len() function returns the number of elements in a list.

# List []   [4] [4,5,6,7]
# Output "Empty"    "Not Empty" "Not Empty"

# My try

# my_list = [4]

# if len(my_list) > 0:
#     print("Not Empty")
# else: 
#     print("Empty")

# My try is bascially the same as solution except other way around and if == 0 print else print

#Option 2

# my_list = [1,2,3,4]

# if not my_list:
#     print("Empty")
# else:
#     print("Not Empty")

# if my_list    | if not my_list
# True          | False

# So the other way to write the same things is;
my_list = [1,2,3,4]

if my_list:
    print("Not Empty")
else:
    print("Empty")
