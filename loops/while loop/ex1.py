n=int (input("Enter how many number u want to generate:"))
if(n<=0):
    print("t{} Invalid Input".format(n))
else:
    print(" number within: {}".format(n))
    i=1
    while(i<=n):
        print("{}".format(i))
        i=i+1
    else:
      print("End of Loop")