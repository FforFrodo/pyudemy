# Write a Python program that prints the string s without 
# the character at index n.
# If the index n is out of range, print the string s intact.
# If the string s is empty, print the string s intact.

# s = Hello, n = 1, ouput = Hllo
# s = World, n = 3, output = Word
# s = Dog, n = 15, output = Dog
# s = "", n = 2, output = ""

# s = "Hello" # H e l l o
# n = 1       # 0 1 2 3 4

# if (len(s) == 0) or (n >= len(s)):
#     print(s)
# else:
#     new_s = ""
#     for i in range(len(s)):
#         if i != n:
#             new_s += s[i]
#     print(new_s)

# Hello - n = 1
# 1st: i = 0 (not n) s[0] = "H" new_s = "H"
# 2nd: i = 1 (is n, do nothing)
# 3rd: i = 2 (not n) s[2] = "l" new_s = "Hl"
# 4th: i = 3 (not n) s[3] = "l" new_s = "Hll"
# 5th: i = 4 (not n) s[4] = "o" new_s = "Hllo"

# Option 2

s = "Hello"
n = 1

if (not s) or (n >= len(s)):
    print(s)
else:
    new_s = ""
    for i in range(len(s)):
        if i != n:
            new_s += s[i]
    print(new_s)