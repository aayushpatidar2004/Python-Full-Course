def readvals():
    n=int(input("Enter How Many Values u have:"))
    if(n<=0):
        return []  # OR  return  list()    returning Empty List
    else:
        lst=[] #empty List
        for i in range(1,n+1):
            val=float(input("Enter {} Value:".format(i)))
            lst.append(val)
        return lst  # Non-empty list
def findsumavg():
    lst=readvals()
    if len(lst)==0:
        return "It is not Possible to find sum average bcoz list is empty"
    else:
        s=0
        for val in lst:
            s=s+val
        avg=s/len(lst)
        return lst,s,avg
def dispsumavg():
     res=findsumavg()
     if(type(res)==tuple):
            print("\tList of Values:",res[0])
            print("\tSum of Values:",res[1])
            print("\tAverage of Values:",res[2])
     elif(type(res)==str):
            print("\t",res)
dispsumavg()
    