def aayush(*ap):
    for value in ap:
        print(value,end=" ")  # ek hi line me print karne ke liye end=" " use kiya hai
    print() # new line ke liye
#main program
aayush(10,20,30,40,50) #function call with 5 arguments
aayush(10,20,30,40) #function call with 4 arguments
aayush(10,20,30) #function call with 3 arguments
aayush(10,20) #function call with 2 arguments
aayush(10) #function call with 1 argument
aayush() #function call with 0 argument
