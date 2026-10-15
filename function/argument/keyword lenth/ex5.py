def aayush(**ap):
    print("--------------------------------------------------------------")
    print("number of arguments:",len(ap))
    print("--------------------------------------------------------------")
    for k,v in ap.items():
        print("\t {}---->{}".format(k,v))
    print("--------------------------------------------------------------")
        #main program4
aayush(sno=10,sname="RS",mm=56,em=70,cname="PSF")
aayush(tno=100,tname="TR",sub1="PYTHON",sub2="Numpy")
aayush(cid=1000,cname="JH",hb="Drawing")
aayush(s=28,name="pooja")
aayush(aus=49)
aayush()

