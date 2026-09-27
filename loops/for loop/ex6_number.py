#Priogram for Cal Product  of N Natural Nums
#NatNumsProductEx1.py
n=int(input("Enter How Many Natural Nums Sum u want:"))
if(n<=0):
    print("\t{} is Invalid Input".format(n))
else:
    print("-------------------------------------------")
    print("Product of First {} Natual Nums".format(n))
    print("-------------------------------------------")
    p=1 # Multiplicative Identity
    for i in range(1,n+1):
        p=p*i # Keeps Track Product of Natuual Nums
        print("\t{}".format(i))
    else:
        print("-------------------------------------------")
        print("Product=",p)
        print("-------------------------------------------")