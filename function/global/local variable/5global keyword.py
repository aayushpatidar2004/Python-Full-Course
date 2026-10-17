def increment():
    global a,b
    a=a + 1
    b=b+1
def modify():
    global a,b
    a=a*2
    b=b*2
def accesvalue():
    c=a+10 # Here We are Just Accessing Global Variable 'a ' But Not Modifying global Var 'a' and No need to write global kwd
    d=b+10 # Here We are Just Accessing Global Variable 'b ' But Not Modifying global Var 'b' and No need to write global kwd
    print("\t\tlocal variable c={} and d={}".format(c,d))
#main program
a,b=10,20 # Here a and b are Called Global Variables
print("\t\tGlobal Variable a={} and b={}".format(a,b)) #10,20
increment() # Here We are Modifying Global Variable 'a' and 'b' So we have to write global kwd in increment() function
print("\t\tGlobal Variable a={} and b={}".format(a,b)) #11,21
modify() # Here We are Modifying Global Variable 'a' and 'b' So we have to write global kwd in modify() function
print("\t\tGlobal Variable a={} and b={}".format(a,b)) #22,
accesvalue() # Here We are Just Accessing Global Variable 'a' and 'b' But Not Modifying global Var 'a' and 'b' So No need to write global kwd in accesvalue() function
print("\t\tGlobal Variable a={} and b={}".format(a,b)) #22,42



