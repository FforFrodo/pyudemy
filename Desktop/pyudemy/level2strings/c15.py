# Write a Python program to count the number of repeated characters in the string s.

# The program must print the total number of repeated characters 
# and a message on the next line displaying the repeated characters 
# separated by a space and sorted alphabetically.

# If there are no repeated characters in the string, 
# print 0 as the total count and None on the next line.
 
# Input     "Hello" "cat"   "AAAAA" "Corporation"
# Output    "1"     "0"     "1"     "2"
#           "l"     None    "A"     "o" "r"

# You might want to keep track of a counter.
# You could store repeated characters in a list. 
# But be careful not to add repeated characters more than once.
# The sorted() function returns a sorted version of a list.
# With print(x, end=" "), you can print a sequence of values on the same line.

# Option 1

# s = "Python"
# # Output = "1" "l"

# repeated_count = 0 # we want a counter variable for counting number of r Chars
# repeated_chars = [] # we want to store whcih chars repeat, in a list to print

# for char in s:  # for every char in string s:
#     if (s.count(char) > 1) and (char not in repeated_chars):
#     # if string.count(characters in string) > 1 and not already in list
#         repeated_count += 1 # increment the count by 1
#         repeated_chars.append(char) # append the char to list

# print(repeated_count) # returns "1" for repeated "l" in "Hello"
# # We dont want to return a list with brackets []

# if len(repeated_chars) > 0: # if repeated char list is 0, we must print 'None', so flip it:
#     for char in sorted(repeated_chars): # for a char in sorted(list) -> aplhabetically
#         print(char, end= " ")   # print the char, end with a space (so next char is on same line)
# else:
#     print(None)


# Option 2

# s = "Hello"

# repeated_count = 0 # counter
# repeated_char = [] # list of characters were repeated

# for char in s:
#     if s.count(char) > 1 and char not in repeated_char:
#         repeated_count += 1
#         repeated_char.append(char)

# print(repeated_count)

# if repeated_char:   # use truthy value
#     print(*sorted(repeated_char), sep= " ")
# else:
#     print(None)

# option 3 - remove counter / just count the length of repeated_char list!

s = "Hello"


repeated_char = [] # list of characters were repeated

for char in s:
    if s.count(char) > 1 and char not in repeated_char:
        repeated_char.append(char)

print(len(repeated_char))

if repeated_char:   # use truthy value
    print(*sorted(repeated_char), sep= " ")
else:
    print(None)