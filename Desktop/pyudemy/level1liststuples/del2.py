# Return indexes which contain an integer as a string
# Input "1a9c8d77f6s"
# Output "024679"
# returns a string of the indexes which contains an integer in a list input.
# Make it as a function

def magic(s):
    restring = ""
    for i in range(len(s)):
        if s[i] >= '0' and s[i] <= '9':
            restring = restring + str(i)

    return restring

print(magic("1a9c8d77f6s"))

#Function def (name)(input):
        # write newstring variable if needed
        # write code
            #write code
        # return

# print(name(input))