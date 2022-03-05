# Write a Python program that prints a version of the string s with all commas replaced by dots.

# Input "this, is, a string!"
# Output "this. is. a string!"

# Input "1,00,9,888"
# Output "1.00.9.88"

# Option 1

# s = "Hello, World!"
# new_s = ""  # set empty string

# comma = "," # St variables for comma and dot
# dot = "."

# for char in s:          # for char in string: # iterates through each char
#     if char == comma:   # if char is a comma:
#         new_s += dot    # new string returns with dot
#     else:               # if char is not comma, newstring returns char intact
#         new_s += char
# print(new_s)

# Option 2

# s = "3,456,344"
# comma = ","
# dot = "."

# print(s.replace(comma, dot))

# Potion 1 as function

def commaReplace(s):
    comma = ","
    dot = "."
    new_s = ""
    for char in s:
        if char == comma:
            new_s += dot
        else:
            new_s += char
    return new_s

print(commaReplace("Hello, World!"))