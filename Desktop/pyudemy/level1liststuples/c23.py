# Write a Python program that removes duplicate elements from a list, 
# only keeping one occurrence of each element in the list.
# The original list should be mutated (modified).
# The program must print the final version of the list.
# Sets are commonly used to remove duplicates from lists and tuples in Python.

# List   [1,1,2,3,4,4]   ["a","a","b","a"]  [1,2,3]  []
# Output [1,2,3,4]       ["a", "b"]         [1,2,3]  []

# Option 1
# my_list = ["a", "a", "b", "a"]
# no_duplicates = list(set(my_list)) # set([]) returns unordered list without duplicates
# print(no_duplicates)
# set does not guarantee order of output elements

# Option 2 - to preserve order use dictionaries 

my_list = ["a", "a", "b", "a"]
no_duplicates = list(dict.fromkeys(my_list))
print(no_duplicates)

# dict.from keys(my_list)
# {1: None, 2: None, 3: None, 4: None}
# will take each unique element from a list and map to none