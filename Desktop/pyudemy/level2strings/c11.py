# Write a Python program that prints a copy of the string s without any spaces.
# Words should be connected in the final string.
# If the string doesn't contain spaces, print it intact.

# Input     "Hello World"   "Have a great day"  "Python"
# Output    "HelloWorld"    "Haveagreatday"     "Python"

# Option 1
# s = "Have a great day"
# new_s = ""

# for char in s:  # iterate over each charater in string
#     if char != " ": # evaluate if char is not = to space
#         new_s += char   # then add the char to the new string

# print(new_s)

# we are building a new string by using a for loop to iterate over each char
# if char is not a space: new string += adds char (from old string iteration)
# prints new string

# Convert to function

def removeSpace(s):
    new_s = ""
    for char in s:
        if char != " ":
            new_s += char
    return new_s

print(removeSpace("Have a nice Day"))