for i in range(5,0,-1):
    print("outer loop val ={}".format(i))
    print("----------")
    j=3
    while(j>=1):
        print("inner loop val ={}".format(j))
        j=j-1
    else:
        print("----------")
        print("inner loop of else")
else:
    print("outer loop of else:")