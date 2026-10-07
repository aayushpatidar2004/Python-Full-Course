def readvalue():
    n=int(input("Enter How Many Values u have:"))
    if(n<=0):
        return []  # OR  return  list()    returning Empty List
    else:
        lst=[]
        for i in range(1,n+1):
            val=float(input("enter {} value:".format(i)))
            lst.append(val)
        return lst  # Non-empty list
def findsumavg():
    lst=readvalue() # Function Chaining
    if len(lst)==0:
       dispsumavg("It is not Possible to find sum average bcoz list is empty") 
    else:
        s=0
        for val in lst:
            s=s+val
        avg=s/len(lst)
        lst.append("sum="+str(s))
        lst.append("avg={}".format(avg))
        dispsumavg(lst)
def dispsumavg(res):
    if(type(res)==list):
        print("\tList of Values:",res[0:-2])
        print("\tSum of Values:",res[-2])
        print("\tAverage of Values:",res[-1])
    elif(type(res)==str):
        print("\t",res)
findsumavg()  # Function Call