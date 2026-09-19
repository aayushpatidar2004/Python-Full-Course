a=float(input("enter the first value:"))
b=float(input("enter the second value:"))
c=float(input("enter the third value:"))
res=a if (a>=b) and (a>c) else b if (b>a) and (b>=c) else c if (c>=a) and (c>b) else "all values are equal"
print("max ({},{},{})={}".format(a,b,c,res))

