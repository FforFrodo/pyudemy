# Write a Python program that checks if the string s ends with a 
# specific sequence of characters denoted by the variable suffix.
# If it does, print True. Else, print False.
# This test should be case sensitive. Therefore, "A" should not be equivalent to "a".
# If the length of the suffix is greater than the length of the string, print False.

# Input     "Hello" "Coding"    "Nora"
# Suffix    "ello"  "eng"       "rowing"
# Output    True    False       "Flase"

# my try, is Option 1!

# s = "Nora"
# suffix = "rowing"

# print(s[-len(suffix):] == suffix)

# s[-len(suffix):] -> String[-length means start counting back from end of array]
# (-) minus means count backwards, (:) at the end] means start from this index
# print that the end of the string by the same length of suffix == suffix itself

# Option 2

s = "Nora"
suffix = "rowing"

print(s.endswith(suffix))
# .endswith(paramter) checks string endswith parameter
# .startswith(parameter checks string starts with parameter)