n=int(input("Enter a number:"))
if(n<=0):
    print("Invalid Input")
else:
    print(" number within: {}".format(n))
    while(n>=1):
        print("{}".format(n))
        n=n-1
    else:
        print("End of Loop")