#Author : Sri Harsha Madabushi
#Date 	:  16/5/2019
#Description:Given a list of int, return True if first and last number of a list is same.

# list1 is a empty list to store input values given to list from user
list1 = []
#to get length of a list
len1  = int(input('enter length of list'))
#multiple values need to be in list1 so using for loop
for num in range(0,len1):
	#entering elements of list
	numbers1 = int(input("enter elements of list"))
	#adding input given above to list
	list1.append(numbers1)
	#printing list1
print(list1)
#comparing first and last values
if (list1[0] == list1[-1]):
	print (True)
else:
	print (False)