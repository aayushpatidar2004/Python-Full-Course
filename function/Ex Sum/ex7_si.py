#Functions for Cal simple Interest
#SimpleIntEx1.py
def readPTRVals():
    P = float(input("Enter Principle Amount:"))
    T = float(input("Enter Time:"))
    R = float(input("Enter Rate of Interest:"))
    return P,T,R
def computeSI():
    P,T,R=readPTRVals() # Here One Function is Calling another Function of same Program--Function Chaining
    si=(P*T*R)/100
    totamt=P+si
    return P,T,R,si,totamt
def dispPTRSI():
    P,T,R,SI,totamt=computeSI() # Here One Function is Calling another Function of same Program--Function Chaining
    print("-" * 50)
    print("\tPrinciple Amount:", P)
    print("\tTime:", T)
    print("\tRate of Interest:", R)
    print("\tSimple Interest:", SI)
    print("\tTOTAL AMOUNT TO PAY:", totamt)
    print("-" * 50)

#Main Program
dispPTRSI() # 