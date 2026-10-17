def increment():
    global a
    a=a + 1
def modify():
    global a
    a=a * 2
#mqin program
a=10 # global variable 
print("the main program value before increment ():",a)  #10
increment()  #function call
print("the main program value after increment ():",a)  #11
modify()  #function call
print("the main program value after modify ():",a)  #22