# Write a Python program that multiplies all the items in a list 
# by the value of the variable factor.
# The program must print the list as the output.
# The program should also allow multiplying the variable factor 
# by a string in case the list contains strings.
# You may assume that the value of factor will be a positive integer.

# Example
# [3,4,5,6]         2   Out= [4,6,10,12]
# ["a", "b", "c"]   3   Out= ["aaa", "bbb", "ccc"]

# Option 1

# my_list = [3,4,5,6]
# factor = 2

# for i in range(len(my_list)):   
#     my_list[i] *= factor

# print(my_list)

# # for i in range() iterates > len() length of > list
# # list[i] each iteration on element *= multiplied by vaiable

# Option 2 enumerate

my_list = [3,4,5,6]
factor = 2

for i, elem in enumerate(my_list):
    my_list[i] = elem * factor

print(my_list)

# enumerate(my_list)
# [(0, 3), (1, 4) (2, 5), (3, 6)]