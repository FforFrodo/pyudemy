# Write a Python program that prints the string s 
# with the character curr_char replaced by the character new_char.

# curr_char and new_char are variables that contain 
# strings with a single character.

# You may assume that new_char will not be an empty string.

# The match must be case-sensitive (do not replace 
# lowercase letters if curr_char is uppercase).

# If no match is found, print the initial string.

# s = "Hello" curr_char = "l" new_char = "s" Out = "Hesso"
# s = "World" curr_char = "W" new_char = "A" Out = "Aorld"
# s = "Python" curr_char = "P" new_char = "x" Out = "xython"
# s = "Python" curr_char = "p" new_char = "a" Out = "Python"

s = "Hello"
new_s = ""

curr_char = "l"
new_char = "s"

for char in s:
    if char == curr_char:
        new_s += new_char
    else:
        new_s += char

print(new_s)

# Hello
# 1st: char = "H" new_s = "H"
# 2nd: char = "e" new_s = "He"
# 3rd: char = "l" new_s = "Hes"
# 4th: char = "l" new_s = "Hess"
# 5th: char = "o" new_s = "Hesso"

# Option 2
s = "Python"
curr_char = "p"
new_char = "a"

print(s.replace(curr_char, new_char))