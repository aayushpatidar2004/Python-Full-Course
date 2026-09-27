n=int(input("enter num: "))
if(n<=0):
    print("invalid")
else:
    for num in range(1,n+1):
        print("mul table",num)
        for i in range(1,11):
            print("{}x{}={}".format(num,i,num*i))
        else:
            print("------------")