i=5
while(i>=1):
    print("outer loop val i={}".format(i))
    print("----------")
  
    for j in range(3,0,-1):
        print("inner loop val ={}".format(j))
    else:
        i=i-1
        print("----------")
        print("inner loop else part")
        print("----------")
else:
    print("outer loop else part")