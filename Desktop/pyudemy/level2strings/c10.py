# Write a Python program that checks if the string s contains all the letters in the alphabet 
# (case-insensitive, so "A" should be equivalent to "a").
# If it does, print True. Else, print False.
# Before comparing the characters, you should convert the string to lowercase.
# If the string contains spaces, ignore them before finding the result.
# You may assume that the string doesn't contain any other symbols, only spaces (possibly).
# Consider these letters as part of the alphabet: 'abcdefghijklmnopqrstuvwxyz'

# To use a constant with all letters of the alphabet, 
# you may use string.ascii_lowercase from the string module. 
# You can import this module by writing import string at the top of your script.
# It can also be helpful to use sets in this problem.

# Inputs                                            Outputs
# "abcdefghijklmnopqrstuvwxyz"                      True
# "The quick brown fox jumps over the lazy dog"     True
# "Hello"                                           False

# Option 1
# import string

# s = "The quick brown fox jumps over the lazy dog"

# set_s = set(s.lower())
# set_s.remove(" ") # remove spaces from the set

# # convert the string to a set to remove duplicates
# # characters and order. copare this set with
# # the set of letters in the constant

# print(set_s == set(string.ascii_lowercase))

# Option 2
#pangram is a senence which uses every letter of alphabet

# import string

# s = "The quick brown fox jumps over the lazy dog"
# is_pangram = True

# for char in string.ascii_lowercase: # iterate over every letter in alphabet
#     if char not in s.lower():   # if char is not in the string
#         is_pangram = False # Update variable to false

# print(is_pangram)

# Option 3
import string

s = "The quick brown fox jumps over the lazy dog"
is_pangram = True

for char in string.ascii_lowercase:
    if char not in s.lower():
        is_pangram = False
        break # Stop loop immediately

print(is_pangram)
