# Write a Python program that reverses the individual words in the string s 
# and changes their capitalization. 
# Uppercase letters should be printed in lowercase and vice versa.

# Assume that the string only contains letters and spaces are used to separate words.

# String    "Hello World"   "Python is Awesome"
# Output    "OLLEh DLROw"   "NOHTYp SI EMOSEWa"

# Solution

# s = "Python is Awesome"
# new_s = ""  # New string for the output
# words_list = s.split(" ") # ["Hello", "World"] Split function! 
# # Split the string at the " ", and return as a list of strings.

# for word in words_list:    # for loop to iterate our list
#     reversed_word = "".join(reversed(word)) 
#     # reversed(word in words_list) .joined by empty string for each letter
#     # reversed_word = word[::-1] # Same thing
#     swapped_case = reversed_word.swapcase() #() stays empty, returns swapped case string
#     new_s += swapped_case + " "
#     # swapped_case is now a list of words
#     # new_s += add list to new string, seperated by a space + " "

# new_s = new_s.rstrip()
# # .rstrip() removes the extra space from the end of the new string

# print(new_s)

# My try

s = "Python is Awesome"
new_s = ""  # New string
word_list = s.split(" ")

for word in word_list:
    reversed_string = s[::-1]
    swapped_case = reversed_string.swapcase()
    new_s = swapped_case + " "

new_s = new_s.rstrip()
print(new_s)

#Bingo!
# We need new string for the output
# word_list and s.split(" ") to retun string as list of words separated at the " "
# for loop word in word_list:
# reversed string = string slicing to reverse -> s[::-1] start to end reversed
# swappedcase = reversedstring.swapcase() function! parameter stays empty
# new_s = ouput list separated with space at end of each element
# string.rstrip() removes the extra space which was added to the end