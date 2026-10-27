from atmexcept import DepositError,WithDrawError,InSuffFundError
bal =500.00
def deposit():
    damt=float(input ("enter your deposit amount:"))
    if(damt<=0):
        raise DepositError
    else:
        global bal
        bal=bal+damt
        print("\tur account balance after deposit:{}".format(bal))
def withdraw():
    global bal
    wamt=float(input("enter  your withdraw amount:"))
    if (wamt<=0):
        raise WithDrawError
    elif ((wamt+500)>bal):
        raise InSuffFundError
    else:
        bal=bal-wamt
        print("\tur account xxxxxxx123 debited with inr:{}".format(bal))
def balenq():
    print("ur account balance:{}".format(bal))
