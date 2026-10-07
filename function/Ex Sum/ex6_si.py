def readPTRVals():
    P=float(input("Enter Principle Amount:"))
    T=float(input("Enter Time:"))
    R=float(input("Enter Rate of Interest:"))
    return P,T,R
def computeSI(P,T,R):
    SI=(P*T*R)/100
    totamt=P+SI
    return SI,totamt
def dispPTRSI(P,T,R,SI,totamt):
    print("-"*50)
    print("\tPrinciple Amount:",P)
    print("\tTime:",T)
    print("\tRate of Interest:",R)
    print("\tSimple Interest:",SI)
    print("\tTOTAL AMOUNT TO PAY:",totamt)
    print("-"*50)

#Main Program
P,T,R=readPTRVals()
SI,totamt=computeSI(P,T,R)
dispPTRSI(P,T,R,SI,totamt)