# even odd
val=int(input("enter any number :"))
if (val>0) and (val%2==0):
    print(" {} is even number".format(val))
else:
    if(val>0) and (val%2!=0):
        print(" {} is odd number".format(val))
    else:
        print(" {} is invalid number".format(val))
print("program is completed")