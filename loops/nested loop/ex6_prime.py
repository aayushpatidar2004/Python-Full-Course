#Program for Generating 1 to N Mul Tables where N is +VE
#InnerLoopEx5.py
n=int(input("Enter the range-In which u want Prime Nums :"))
if(n<=1):
    print("\t{} is Invalid Input".format(n))
else:
    print("-----------------------------------------------")
    print("List of Primes within {}".format(n))
    print("-----------------------------------------------")
    for num in range(2,n+1):
        res=True
        for i in range(2,num):
            if(num%i==0):
                res=False
                break # Just Comes out-off iner loop
        if(res):
            print("\t{}".format(num))
    else:
        print("-------------")