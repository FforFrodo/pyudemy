#Youtube
# Return indexes which contain an integer as a string
# Input [0,1,2,"A","B","D","H",5,2]
# Output [0,1,2,7,8]

# my_list = [0,1,2,"A","B","D","H",5,2]
# new_list = ""

# for i in range(len(my_list)):
#     if my_list[i]>= 0 and my_list <= 9:
#         new_list = new_list + str(i)
#     print(new_list)

def processString(s):
    res = ""
    for i in range (len(s)):
        if s[i] >= '0' and s[i] <= '9':
            res = res + str(i)
    return res

print(processString("012ABDH52"))