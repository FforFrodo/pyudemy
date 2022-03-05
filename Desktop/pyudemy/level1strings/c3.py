# Write a Python Program that prints the reversed version of a string.
# The program must preserve uppercase and lowercase letters.
# If the string is empty, print it intact.
#input "Hello" , output "olleH", input = "" , output = ""

# Option 1 - string slicing
# s = "Hello"

# print(s[::-1]) 

# string[start:stop:step]
# string[::step] /default for start /default for step
# -1 steps backward to reverse the string

# Option 2 - assign to a variable

# s = "Hello"

# reversed_word = s[::-1]
# print(reversed_word)

# Option 3
s = "Hello"

reversed_word = "".join(reversed(s))
print(reversed_word)

# reversed("Hello") -> ["o", "l", "l", "e", "H"]
# "".join(["o", "l", "l", "e", "H"])

# "".join joins all elements in the list with empty string ""