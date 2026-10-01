#Function Def for Adding Two Numbers
# INPUT         : Input Taking Inside of Function Body
# PROCESS       : Processing Done in Function Body
# OUTPUT        : Output Returned to Function Call
#ApproachEx2.py
def sumop():
    k=float(input("Enter First Number:"))
    v=float(input("Enter Second Number:"))
    r=k+v
    return k,v,r
#Main Program
x,y,z=sumop() # Function Call  with Multi line assignment
print("Sum({},{})={}".format(x,y,z))
print("---------OR------------------")
res=sumop()  # Function Call  with Single line assignment
#Here res is an object of <class, tuple>
print("Sum({},{})={}".format(res[0],res[1],res[2]))