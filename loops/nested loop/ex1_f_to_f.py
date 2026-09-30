
for i in range(1,6):
    print("Outer Loop: Val of i={}".format(i))
    print("--------------------------------------")
    for j in range(1,4):
        print("\tInner Loop: Val of j={}".format(j))
    else:
        print("----------------------------------------")
        print("Coming out-off Inner Loop-going to outer Loop")
else:
    print("i am from outer loop else")
    