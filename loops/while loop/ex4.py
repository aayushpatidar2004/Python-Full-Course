n=int(input("Enter a number:"))
if(n<=0):
    print("Invalid Input")
else:
    print(" number within: {}".format(n))
    i=2
    while(i<=n):
        print("{}".format(i))
        i=i+2
    else:
      print("End of Loop")