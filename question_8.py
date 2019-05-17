# Author : Sri Harsha Madabushi
#Date    : 16/5/2019
"""Description: Given a string and an int n, remove characters from string at every n position  and return a new string and then new list for that string.
   ex- if n=3 then it should remove every 3rd element.""" 


string1 = input("enter a string")
string2 = list(string1)
string3 = []
# Accepting value of n from user
n = int(input("enter value of n to remove characters at every n position"))
# assigning value of n to a
a = n
# caluculating length of string
len1 = len(string1)
# iterating till end of list
for i in range(0, len1):
    # comparing n-1 with dummy variable
    if (i == n - 1):
        # incrementing value of n
        n = n + a
    else:
        string3.append(string1[i])
print(string3)
		

	

