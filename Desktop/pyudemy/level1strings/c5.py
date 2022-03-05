# Write a Python program that prints the string s without the characters located at even indices.
# If the string is empty or only has one character, print it intact.
# Input -> "Coding" Execpted output -> "oig"
# Input "Pizza" -> "iz"
# "Python" -> "yhn"
# "A" -> "A"
# "" -> ""

# Option 1

# s = "Coding"    # C o d i n g       len(s) -> 6
# new_s = ""      # 0 1 2 3 4 5
#                 # 0 .... len(s)-1 
# for i in range(len(s)):
#     if i % 2 != 0:
#         new_s += s[i]

# print(new_s)

# range(len(s)) -> 0, 1, 2, ... len(s)-1

# 1st: i = 0    new_s = ""
# 2nd: i = 1    s[1] = "o"  new_s = "o"
# 3rd: i = 2 (even)         new_s "o"
# 4th: i = 3    s[3] = "i"  new_s = "oi"
# 5th: i = 4 (even)         new_s = "oi"
# 6th: i = 5    s[5] = "g"  new_s = "oig"

# Option 2

s = "Coding"
new_s = ""

for i in range(1, len(s), 2):
    new_s += s[i]

print(new_s)

# range(1, len(s), 2)
# 1, 3, 5, 7, ..., len(s)-1

# 1st: i = 1    s[1] = "o"  new_s = "o"
# 2nd: i = 3    s[3] = "i"  new_s = "oi"
# 3rd: i = 5    s[5] = "g"  new_s = "oig"
# Stops iterating by 2 as length is 6, so only 3 times