# Write a Python program to convert a string s to lowercase, 
# sort the characters of each word in alphabetical order, and print the resulting string.
# You may assume that the string only contains letters and spaces to separate the words.
# Spaces should be preserved in the final string.

# In Python, uppercase letters come before lowercase letters in alphabetical order.
# The sorted() function can be used to get a sorted list with the characters in a string.

# Input     "Hello" "Awesome"   "Wonderful World"
# Output    "ehllo" "aeemosw"   "deflnoruw dlrow"

# Option 1

# s = "Hello World"
# new_s = ""

# word_list = s.split(" ") # -> ["Hello", "World"]

# for word in word_list: # for ever word in the list:
#     lowercase_word = word.lower() # lower() converts to lowercase
#     sorted_word = "".join(sorted(lowercase_word))   # sort letters alphabetically and join
#     new_s += sorted_word + " "  # sorted words are added to new string with space at the end 

# new_s = new_s.rstrip()

# print(new_s)

# Option2

s = "Wonderful World"   # Input String
new_s = ""          # New string Output

words_list = s.split(" ")   # Split the string at spaces, return as list

for word in words_list: # for loop for each word in the words_list:
    new_s += "".join(sorted(word.lower())) + " "
    # add word.lower as sorted + a space, to new string, joined by "" at each letter
    # This is very similar to my initial intution before i deleted 

new_s = new_s.rstrip()

print(new_s)