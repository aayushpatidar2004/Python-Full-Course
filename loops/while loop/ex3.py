n=int(input("Enter a number:"))
if(n<=0):

    print("Invalid Input")
else:
    print(" number within: {}".format(n))
    i=1
    while(i<=n):
        if(i%2==0):
            print("{}".format(i))
        i=i+1
    else:
        print("End of Loop")