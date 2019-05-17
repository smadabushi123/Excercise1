#Author : Sri Harsha Madabushi
#Date     : 17/05/2019
"""Description:Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
	Suppose the following input is supplied to the program:
	Hello world
	Practice makes perfect
	Then, the output should be:
	HELLO WORLD
	PRACTICE MAKES PERFECT"""
	
#Asking user to input a string
string1 = input("please enter a string :")
#using capitalize function to capitalize entire string
string2 = string1.upper()
#printing the every character of a  string  before converting to upper case
print("string before converting in to upper case :",string1)
#printing the every character of a  string in upper case
print("string  in upper case is :",string2)
