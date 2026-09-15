# WAP to find the greatest of 3 numbers entered by the user.

first =int(input("enter the first num : "))
second =int(input("enter the second num :"))
third =int(input("enter the third num : "))

if (first>second>third):
    print("first is greater")
elif(second>third):
    print("second is greater")
else:
    print("third is greater")