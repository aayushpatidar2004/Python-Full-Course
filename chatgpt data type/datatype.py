
# FLOAT
# price = 99.50
# print(price,type(price))



# STRING

# name ="AAYUSH"
# print(name)


# BOOL

# a=10
# b=20
# print(a>b)

# TYPE CHECK

# a=10
# b=10.5
# c="python"
# d=True
# print(a,type(a))
# print(b,type(b))
# print(c,type(c))
# print(d,type(d))


# arithmetic op


# a=20
# b=5
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# # print(a%b) modulo
# print(a//b) #floor division/



# a= "100"
# b=int(a)
# print(b,type(b))


# lst=[10,20,30,40,50]
# # print(lst,type(lst))
# print(lst[0])


# lst=[10,20,30,40,50]
# lst[1]=200
# print(lst)


# tpl=(10,20,30,40)
# print(tpl[2])

# s={10,20,20,30}
# print(s)


# dicto= {
#     "name" :"aayush",
#     "age" : 20,
#     "course" : "python",

# }
# print(dicto)


# ram= int(input("enter the age :"))
# print(ram>=18)


# num =int(input("enter the  num :"))
# if (num%2==0):
#     print("even")
# else:
#     print("odd")

# num1 =int(input("enter the  num :"))
# num2 =int(input("enter the  num :"))
# if (num1>num2):
#     print("num1 is greater")
# else:
#     print("num2 is greater")


# num=[10,20,30,40,50]
# print(sum(num))



# Ek number input lekar uska square aur cube print karo.
# num  = int (input("enter square"))
# square=num**2
# cube=num**3
# print("square",square)
# print("cube",cube)


# 1 se 10 tak numbers print karo using a for loop.

# for i in range(1,11):
#     print(i)


# Ek number input lekar uska factorial find karo.

# num=int(input("enter the num : "))
# fact=1
# for i in range(1,num+1):
#     fact=i*fact
#     print(fact)
# -----------------------------------------------------------

# Write a Python program to check whether a number is even or odd

# num=int (input("enter num :"))

# if (num%2)==0:
#     print("even")
# else:
#     print("odd")

    # ------------------------------------------------------------------

# Write a program to check whether a given number is positive, negative, or zero.

# num=int(input("enter the  num : "))
# if num>0:
#     print("possitive")
# elif num<=-1:
#     print("nagative")
# else:
#     print("zero")
# ----------------------------------------------------------

# Largest of Two Numbers
# Take two numbers as input and print the largest number.

# a=int(input("enter the first num :"))
# b=int(input("enter the second num :"))
# c=int(input("enter the third num :"))
# # if a>b:
# #      print("a largest number is ",a)

# # else:
# #      print("largest number is ",b)

#     #  or
# print("largest num :",max(a,b,c))
# ---------------------------------------------------------------

# Sum of 1 to N
# Take N as input and calculate:

# num=int(input("enter the first num :"))
# sum=0
# for i in range(1,num+1):
#    sum=sum+i
#    print("sum =",sum)
# --------------------------------------------------

# Multiplication Table
# Take a number as input and print its multiplication table from 1 to 10.

# n=int(input("enter the first num :"))

# for i in range(1,11):
#     print( n,"x",i,"=",n*i)
# ----------------------------------------------------------

# Q17. Count Digits
# Write a program to count the number of digits in an integer.

# a=int(input(" enter number:"))

# count=len(str(a))

# print("number of digit =",count)


r=(input(" enter number:"))
print("revers",r[::-1])
