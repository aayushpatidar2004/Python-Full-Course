#Program for Demonstrating Default Arguments Mech
#DefaultArgsEx2.py
def  dispstuddata(sno,sname,marks,crs="PYTHON",city="HYD"):
	print("\t{}\t{}\t{}\t{}\t{}".format(sno,sname,marks,crs,city))

#Main Program
print("-"*50)
print("\tSNO\tNAME\tMARKS\tCOURSE\tCITY")
print("-"*50)
dispstuddata(10,"RS",34.56) # Function  Call-
dispstuddata(20,"DR",54.16) # Function  Call-
dispstuddata(30,"SR",34.86) # Function  Call-
dispstuddata(40,"JH",52.16) # Function  Call-
dispstuddata(50,"MB",24.86) # Function  Call-
dispstuddata(60,"DT",11.34,city="USA")
dispstuddata(city="RSA",sno=70,crs="HTML",sname="PT",marks=44.44)
print("-"*50)