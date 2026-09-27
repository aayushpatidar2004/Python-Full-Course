#Program for Accepting List of Values from Key Board and
#Find their sum and average
#ListValsSumEx2.py
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
        print("Sum={}".format(sum(lst)))
        print("Avg={}".format(sum(lst)/len(lst)))
        print("--------------------------------")
