#Program for Demonstrating Default Arguments Mech
#DefaultArgsEx1.py
def  dispstuddata(sno,sname,marks,crs="PYTHON"):
	print("\t{}\t{}\t{}\t{}".format(sno,sname,marks,crs))

#Main Program
print("-"*50)
print("\tSNO\tNAME\tMARKS\tCOURSE")
print("-"*50)
dispstuddata(10,"RS",34.56) # Function  Call-
dispstuddata(20,"DR",54.16) # Function  Call-
dispstuddata(30,"SR",34.86) # Function  Call-
dispstuddata(40,"JH",52.16) # Function  Call-
dispstuddata(50,"MB",24.86) # Function  Call-
print("-"*50)