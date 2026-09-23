#Program for Generating 1 to N where N is +VE
#ForLoopEx1.py
n=int(input("Enter How Many Numbers u want to Generate:")) # n=5
if(n<=0):
    print("\t{} is Invalid Input".format(n))
else:
    print("-" * 50)
    print("Numbers within:{}".format(n))
    print("-" * 50)
    for i in range(1,n+1):
        print("\t{}".format(i))
    else:
        print("-" * 50)