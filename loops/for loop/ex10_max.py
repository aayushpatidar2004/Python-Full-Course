n=int(input("enter values is : "))
if(n<=0):
    print("invalid ")
else:
    lst=list()
    for i in range(1,n+1):
        val=float(input("Enter {} Value: ".format(i)))
        lst.append(val)
    else:
        print("list of value=",lst)
        maxv=max(lst)
        minv=min(lst)
        print("maxv =",maxv)
        print("minv=",minv)