# Write a Python program that checks if the string s starts with 
# the sequence of characters denoted by the variable prefix.

# If it does, print True. Else, print False.

# This test should be case sensitive. For example, "A" should not be equivalent to "a".
# If the length of the prefix is greater than the length of the string, print False.

# Input     "Hello World"  "What"  "Dog"
# Prefix    "Hell"          "tltl"  "Octopus"
# Output    True            False   False


# my try 

# If s contains prefix return True
#     else return False

# s = "Hello World"
# prefix = "Hell"

# for chars in s.len(prefix):
#     if chars == prefix and chars <= prefix:
#         print("True")
#     else:
#         print("false")
# fail

# Option 1

# s = "Coding"
# prefix = "Con"

# print(s[:len(prefix)] == prefix)

# String slicing.
# We define the string and the prefix.
# We simply print string sliced by the length of the prefix as equal to prefix
# This returns true or false.
# [Start : Step : Stop] -> [Start at default 0 until :length of (prefix)]

# H e l l o ->      len(Hello) = 5
# 0 1 2 3 4
# Prefix = "Hell"   len("Hell") = 4
# s[:len(prefix)] -> s[:4] does s until the length of preix == prefix?

# Option 2

s = "Hello"
prefix = "He"

print(s.startswith(prefix))
# .startswith() method checks a string startswith(parameter)