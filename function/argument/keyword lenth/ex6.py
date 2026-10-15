def findtotalmarks(sno,sname,cls,**submarks):
    print("----------------------------")
    print("\tstudent number=",sno)
    print("\tstudent name =",sname)
    print("\tstudent class=",cls)

    if(len(submarks)!=0):
        totalmarks=0
        print("________________________________")
        print("\tsubject\t\tmarks")
        for subject,marks in submarks.items():
            print("\t{}\t{}".format(subject,marks))
            totalmarks=totalmarks+marks
        print("\tTotal marks =",totalmarks)
    print("----------------------------------")
#main program
findtotalmarks(10,"pooju","X",eng=80,hindi=90,py=95,chem=88,telgu=70,math=98)
findtotalmarks(20 ,"pooju","XII",eng=88,HIndi=99,CHem=77,PHY=88)
findtotalmarks(30,"Dinesh","B.Tech",OS=50,DBMS=65,CNN=55,JavaLab=30)
findtotalmarks(40,"Trump","Politics",Eco=70,Civics=50)
findtotalmarks(50,"Rossum","Research")