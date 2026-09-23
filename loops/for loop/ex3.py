#Program for Generating Eve Numbers within N is +VE
#ForLoopEx2.py
n=int(input("Enter How Many Numbers u want to Generate:")) # n=5
if(n<=0):
    print("\t{} is Invalid Input".format(n))
else:
    print("-" * 50)
    print("Even Numbers from 2 to N".format(n))
    print("-" * 50)
    for i in range(2,n,2):
        print("\t{}".format(i))
    else:
        print("-" * 50)