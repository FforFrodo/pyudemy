# Return indexes which contain an integer as a string
# Input [0,1,2,"A","B","D","H",5,2]
# Output [0,1,2,7,8]
# returns a string of the indexes which contains an integer in a list input.
# Make it as a function

def proccessString(s):      # Define function(inputstring):
    new_string = ""         # Declare New_string emtpy (strings are not mutable)
    for i in range(len(s)): # for loop index in range(lengthofstring(input string)):
        if s[i] >= '0' and s[i] <= '9': # if string[index] greater/equal 0 and less/equal 9:
            new_string = new_string + str(i) # newstring = newstring + str(index)

    return new_string   # return result of code

print(proccessString("012ABDH52")) # print function(inputstring)