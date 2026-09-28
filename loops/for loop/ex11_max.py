

#Program for accepting List of Values and Find Max and Min
#FindingMaxMinElementsEx1.py
n=int(input("Enter How Many Nums u have:"))
if(n<=0):
    print("\t{} is Invalid Input".format(n))
else:
    lst=list()  # Create empty list
    for i in range(1,n+1):
        val=float(input("Enter {} Value:".format(i)))
        lst.append(val)
    else:
        print("List of Values=",lst) # [10, 2, 13, 4, 15, 6, 17, 8, 11]
        #Code for Getting Max  from List of Values
        maxv=lst[0] # Maxv=17
        for val in lst[1:]:
            if val>maxv:
                maxv=val
        else:
            print("Max Value=",maxv)
            # Code for Getting Min  from List of Values
            ## [10, 2, 13, 4, 15, 6, 1, 8, 11]
            minv=lst[0]    #minv=1
            for val in lst[1:]:
                if val<minv:
                    minv=val
            else:
                print("Min Value=",minv)
