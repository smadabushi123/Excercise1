# Name : Sri Harsha Madabushi
# Date : 16/5/2019
"""Description : Create a program that asks the user to enter their name and their age. 
     Print out a message addressed to them that tells them the year when they will turn 100 years old."""
#accepting name from user
name = input("Please enter your name")	 	 
#accepting age from user
age = int(input("Please enter your age"))
#To caluculate difference between 100 and current age 
age_hundred = 100 - age
#adding age_hundred to current year 2019 will give user , year when he bwill be hundred
year        = 2019 + age_hundred
print(name,"will be hundred years old by", year)	 