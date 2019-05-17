#Author : Sri Harsha Madabushi
#Date   : 16/5/2019
"""Description :Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
	Suppose the following input is supplied to the program:
	without,hello,bag,world
	Then, the output should be:
	bag,hello,without,world"""
#accepting the list length from user
len1 = int(input("enter length of the string"))
#defining an empty list to store elements which will be given by user
list1 = []
#using for loop as multiple values need to be stored in list1
for i in range(0, len1):
	#accepting list items from user
    string1 = input("enter strings ")
	#appending those items in to list
    list1.append(string1)
	#printing list before sorting
print("list before sorting is :",list1)
#as there are multiple values in list we are using for loop
for i in range(0, len1):
#sorting the list busing sort function
    list1.sort()
	#printing list AFTER SORTING
print("list after sorting :",list1)






