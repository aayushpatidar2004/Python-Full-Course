#Function Def for Adding Two Numbers
# INPUT         : Input Taking From Function Call
# PROCESS       : Processing Done in Function Body
# OUTPUT        : Output Returned to Function Call
#ApproachEx1.py



def sumop (k,v): # here k,v are called formal 
    r=k+v #here r is called local variable
    return r
a=float(input("enter value1 :"))
b=float(input("enter value2 :"))
res=sumop(a,b)
print("sum of ({} ,{} ={})".format(a,b,res))

k=float(input("enter value:"))
v=float(input("enter value"))
res=sumop(k,v)
print("sum of ({},{}={})".format(k,v,res))