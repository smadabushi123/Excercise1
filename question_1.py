"""Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included).
     The numbers obtained should be printed in a comma-separated sequence on a single line."""
list7 = [] #empty list to store all numbers which are divisible by 7
list5 = [] #empty list to store all numbers which are divisible by 5	 
for numbers in range(2000,3201):# range is used to get all the numbers between 2000 and 3200 as we need to include 3200  i kept end limit as 3201
	if (numbers%7==0):  #finding all the numbers which are divided by 7
		list7.append(numbers)
for numbers1 in list7:
	if(numbers%5==0):
		list7.remove(numbers1)
print(list7)
	