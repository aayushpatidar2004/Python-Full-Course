a=float(input("enter the first value:"))
res="positive" if a>0 else "negative" if a<0 else "zero"
print("{} is {}".format(a,res))