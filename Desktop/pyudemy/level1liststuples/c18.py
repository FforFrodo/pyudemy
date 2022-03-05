# Write a Python program that prints the elements of a list on the same line.
# The elements should be separated only by a space (not by a comma).
# The output should not include the opening and closing square brackets [ ].

# List [3, 4, 5, 6] ["a", "b", "c"]
# Output 3 4 5 6   | a b c

# # Option 1
# my_list = [3, 4 ,5, 6]

# for elem in my_list:
#     print(elem, end=" ")

# # Option 2

my_list = [3, 4, 5, 6]

print(*my_list, sep=" ")