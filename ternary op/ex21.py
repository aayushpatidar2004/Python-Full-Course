a=int(input("enter a number:"))
b=int(input("enter a number:"))

re="maximum" if a>b else "minimum" if a<b else "both are equal"
print("between {} and {} the {} is {}".format(a,b,re,a ))