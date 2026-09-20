#program for Cal SI By accepting P,T and R Values

p=float(input("enter principle amount : "))
t=float(input("enter time in years : "))
r=float(input("enter rate of interest : "))
if(p>0) and (t>0) and (r>0):
    si=(p*t*r)/100
    print("rejult of simple interest")
    print("principle amount : {}".format(p))
    print("time : {}".format(t))
    print("rate of interest : {}".format(r))
    print("simple interest : {}".format(si))
if(p<=0):
    print(" {} is invalid  principle amount".format(p))
if(t<=0):
    print(" {} is invalid time".format(t))
if(r<=0):
    print(" {} is invalid rate of interest".format(r))