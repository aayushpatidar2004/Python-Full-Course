a=10
b=20
c=30
d=40   # a,b,c,d are global variable
def operration():
    x=100
    y=200
    z=300
    k=400 #x,y,z,k are local variable
    res=a+b+c+d+x+y+z+k
    print("the result of global and local variable is:",res)
#main program
operration()