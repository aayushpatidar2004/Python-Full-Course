i=1
while(i<=5):
    print("outer loop val i={}".format(i))
    print("----------")
    j=1
    while(j<=3):
        print("inner loop val j ={}".format(j))
     
        j=j+1
    else:
        print("----------")
        i=i+1
else:
    print("----------------")