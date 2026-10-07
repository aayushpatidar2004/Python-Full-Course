#Functions for Finding Sum and Avg for List of Values
#FindSumAvg1.py
def readVals():
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
    lst=readVals() # Function Chaining
    #Here lst may be empty (length=0)  or non-empty (length>0)
    if len(lst)==0:
        return "It is not Possible to find sum average bcoz list is empty"
    else:
        s=0
        for val in lst:
            s=s+val
        avg=s/len(lst)
        return lst,s,avg
def dispsumavg():
    res=findsumavg() # here res can be either <class,str> or <class, tuple>
    if(type(res)==tuple):
        print("\tList of Values:",res[0])
        print("\tSum of Values:",res[1])
        print("\tAverage of Values:",res[2])
    elif(type(res)==str):
        print("\t",res)

#Main Program
dispsumavg()