#Function Def for Adding Two Numbers
# INPUT         : Input Taking From Function Call
# PROCESS       : Processing Done in Function Body
# OUTPUT        : Output Displayed in Function Body
#ApproachEx3.py
def addop(k,v):
    r=k+v
    print("Sum({},{})={}".format(k,v,r))
#Main Program
a=float(input("Enter First Value: "))
b=float(input("Enter Second Value: "))
addop(a,b) # Function Call