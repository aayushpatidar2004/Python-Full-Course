num1=int(input("enter a number:"))
num2=int(input("enter a number:"))
res=num1-num2 if num1>num2 else num2-num1
print("Absolute difference is {}".format(res))