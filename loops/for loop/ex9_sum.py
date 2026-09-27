n=int(input("enter natural num :"))
if(n<=0):
    print("invalid")
    
else:
    print("sum of {} num".format(n))
    s=0
    for i in range(1,n+1):
        s=s+i
        print(i)
    else:
        print("sum",s)