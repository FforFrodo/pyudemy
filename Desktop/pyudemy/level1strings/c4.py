# Write a Python program that prints the first 
# and last three characters of the string s as a single string.
# If the string has less than six characters, 
# print an empty string (blank output).

# # Option 1
#                 # len(s) -> 9
# s = "Wonderful" # W o n d e r f u l
#                 # 0 1 2 3 4 5 6 7 8

# if len(s) < 6:
#     print("")
# else:           # "Won" + (len= 9) -3= 6, count from 6 until end,== "ful"
#     new_string = s[:3] + s[len(s)-3:]
#     print(new_string)

# s[:3] -> Start at default i (0) until 3 (3 is not inclusive, stops at 3)
# so 0, 1 , 2 ->  "W, o, n"

# Option 2- set variable for repeated conditional value

s = "Wonderful"
num_chars = 3

if len(s) < num_chars*2:
    print("")
else:           # "Won" + (len= 9) -3= 6, count from 6 until end,== "ful"
    new_string = s[:num_chars] + s[len(s)-num_chars:]
    print(new_string)