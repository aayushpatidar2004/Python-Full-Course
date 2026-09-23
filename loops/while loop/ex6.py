n=int(input("Enter Any Number for Generating Mul Table:"))
if(n<=0):
    print("\t{} is Invalid Input".format(n))
else:
    print("-" * 40)
    print("Mul Table for :{}".format(n))
    print("-" * 40)
    i=1
    while(i<=10):
        print("\t{} x {}={}".format(n,i,n*i))
        i=i+1
    else:
        print("-"*40)