# Write a Python program that prints the character at index i in the string s.
# If the index is out of range, the program should print "i is out of range"
# If the string is empty, the program should print "Empty String"

# Expected output 
# String= "Hello" , i = 2 , Output = "l"
# string ="" i = 3 , Output = Empty string
# string = "world" , i = 15 , output = "i is out of range"

# s = "Hello" # H e l l o
# i = 0       # 0 1 2 3 4

# if len(s) == 0:
#     print("Empty String")
# elif i < len(s):
#     print(s[i])
# else:
#     print("i is out of range")

#---Option2

s = "Hello" # len = 5
i = 1 # output e

# if string is not empty, and use if not, then it will evaluate to True
# checking if string is empty 'if there is not a string then pass True'

if not s:
    print("Empty String")
elif i < len(s): # if i is less than length of string
    print(s[i])  # print s[value at index of s]
else:
    print("i is out of range") # else i is greater than length of s, print out of range 