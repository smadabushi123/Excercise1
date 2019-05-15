# Author : Sri Harsha Madabushi
#Date    : 15/05/2019
#Description
"""Write a program that calculates and prints the value according to the given formula:
	Q = Square root of [(2 * C * D)/H]
	Following are the fixed values of C and H:
	C is 50. H is 30.
	D is the variable whose values should be input to your program in a comma-separated sequence.
	Example
	Let us assume the following comma separated input sequence is given to the program:
	100,150,180
	The output of the program should be:
	18,22,24"""

# importing math module as it will be used for using square root function	

import math
c = 50                                # initializing value  of c
h = 30                                #initializing value  of h
# initializing an empty list to store input from user
list1 = []
# initializing an empty list to store output
list2 = []
#calculating length of list
len1 = int(input("please for how many numbers formula need to be applied"))
#entering values of d in to list1
for i in range(0,len1):
	d = int(input("enter numbers to which formula need to be applied"))
	list1.append(d)
#for using d in formula by assigning  to dummy variable j
for j in list1:
    print(j)
    q  =  round(math.sqrt((2*c*j)/h))
    list2.append(q)
print("value of q is : ",list2)
