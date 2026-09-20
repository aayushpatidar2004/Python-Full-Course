#Program for accepting any +VE Numerical Integer Value
#and decide whether It is Even OR Odd
val=int(input("enter any +ve value : "))
if(val>0) and (val%2==0):
    print(" {} is  Even".format(val))
if(val>0) and (val%2!=0):
    print(" {} is Odd".format(val))
if (val<=0):
    print(" {} is invalid input".format(val))