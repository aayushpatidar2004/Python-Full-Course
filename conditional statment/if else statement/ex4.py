#simple intrest
p=float(input("enter principle amount : "))
t=float(input("enter time in years : "))
r=float(input("enter rate of interest : "))
if((p>0) and (t>0) and (r>0)):
    si=(p*r*t)/100
    print("result of simple interest")
    print("simple interest is : {}".format(si))
else:
    if(p<=0):
        print(" {} is invalid principle amount".format(p))
    if(t<=0):
        print(" {} is invalid time".format(t))
    if(r<=0):
        print(" {} is invalid rate of interest".format(r))
        
print("invalid input")