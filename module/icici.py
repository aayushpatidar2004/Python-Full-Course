#icici.py<----File Name<----Module Name
bname="ICICI"
addr="AMPT-HYD"  # Here bname,ampt are Called Global Variables
def simpleint():  # Function Definition
    P = float(input("Enter Principle Amount:"))
    T = float(input("Enter Time:"))
    R = float(input("Enter Rate of Interest:"))
    # Cal si and totamt
    si = (P * T * R) / 100
    totamt = P + si
    print("-" * 50)
    print("\tResults of Simple Interest")
    print("-" * 50)
    print("\t\tPrinciple Amount:", P)
    print("\t\tTime:", T)
    print("\t\tRate of Interest:", R)
    print("\t\tSimple Interest:", si)
    print("\t\tTotal Amount to Pay:", totamt)
    print("-" * 50)