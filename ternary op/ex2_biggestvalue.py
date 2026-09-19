a=float(input("enter the first value:"))
b=float(input("enter the second value:"))
res=a if a>b else b if b>a else "both are equal"
print("max ({},{})={}".format(a,b,res))