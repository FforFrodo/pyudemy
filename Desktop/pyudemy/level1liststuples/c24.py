# Write a Python program that counts the number of elements in a list with value greater than 3.
# You may assume that the list only contains numbers.
# Print the final count.

# You will need to define a variable that will act as the counter 
# and print the value of this counter.
# "Greater than" means strictly greater than a value. 
# It does not include cases where the value is equal to 3.
# You may want to use a for loop, list comprehension, or generator expressions.

# List      [1,2,3,4,5,6,7]
# Output    4

# Option 1 (My function version)
# def greater3(e):
#     counter = 0
#     for elem in e:  # for every element in list
#         if elem > 3:    # if elem greater than 3 (and condition is true)
#             counter += 1    # add 1 to counter incrementally

#     return counter  # return counter

# print(greater3([1,2,3,4,5,6,7]))    # print function(input)

# # Option 2
# my_list = [1,2,3,4,5,6,7,8,9]   # Output 6

# count = sum(1 for elem in my_list if elem > 3)
# # sum all elements in sequence by this expression (greater than 3)
# print(count)

# Option 2 as function

def great3(input):
    count = sum(1 for elem in input if elem > 3)
    return count

print(great3([1,2,3,4,5,6,7,8,9]))