"""Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.
  Suppose the following input is supplied to the program:
    34,67,55,33,12,98
    Then, the output should be:
    ['34', '67', '55', '33', '12', '98']
    ('34', '67', '55', '33', '12', '98')"""


list1 = []
len1 = int(input("enter how many numbers that need to be in list and tuple"))#accepting length of list and tuple from users 
for dummy in range(0,len1): # as we need to enter multiple values in to list and tuple we are using for loop
    numbers = int(input("enter numbers that need to be in list and tuple"))#accepting imput from user
    list1.append(numbers)# making a list using those numbers
    tuple1 = tuple(list1)#converting list in to tuple by using tuple() constructor
print(list1)
print(tuple1)
