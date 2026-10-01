def sumop (k,v): # here k,v are called formal 
    r=k+v #here r is called local variable
    return r
a=float(input("enter value1 :"))
b=float(input("enter value2 :"))
res=sumop(a,b)
print("sum of ({} ,{} ={})".format(a,b,res))

k=float(input(""))
v=float(input(""))
res=sumop(k,v)
print("sum of ({},{}={})".format(k,v,res))