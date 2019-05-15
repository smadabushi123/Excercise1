"""Write a program which can compute the factorial of a given numbers.The results should be printed in a comma-separated sequence on a single line
"""
n = int(input("Enter length of the list"))
list1 = []
for i in range(0, n):
    a = int(input())
    list1.append(a)
print(list1)

for j in range(0,n):
    b= list1[j]
    
    fac = 1

    for i in range(1, b+1):
        fac = fac * i

    print("factorial of ", b, " is ", fac)