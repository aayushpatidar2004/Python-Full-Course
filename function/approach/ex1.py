def sumop (k,v): # here k,v are called formal 
    r=k+v #here r is called local variable
    return r

#main program
res=sumop(10,20)#function call
print("sum=",res)
r=sumop(100,200)
print("sum=",r)