#Program for Accepting List of Values from Key Board and
#Find their sum and average
#ListValsSumEx1.py
n=int(input("Enter How Many Nums u have:"))
if(n<=0):
    print("\t{} is Invalid Input".format(n))
else:
    lst=list()  # Create empty list
    for i in range(1,n+1):
        val=float(input("Enter {} Value:".format(i)))
        lst.append(val)
    else:
        print("--------------------------------")
        print("List of Values")
        print(lst)  # lst=[10,20,30,40,50]
        print("--------------------------------")
        #Code for Finding Sum of List of Values
        s=0
        for val in lst:
            s=s+val
        else:
            print("Sum={}".format(s))
            print("Avg={}".format(s/len(lst)))
            print("--------------------------------")
