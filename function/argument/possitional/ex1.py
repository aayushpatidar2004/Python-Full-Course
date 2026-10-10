#Program for Demonstrating Possitional Arguments
#PossArgsEx1.py
def  dispstuddata(sno,sname,marks):
	print("\t{}\t{}\t{}".format(sno,sname,marks))

#Main Program
print("-"*50)
print("\tSNO\tNAME\tMARKS")
print("-"*50)
dispstuddata(10,"RS",34.56) # Function  Call-
dispstuddata(20,"DR",54.16) # Function  Call-
dispstuddata(30,"SR",34.86) # Function  Call-
dispstuddata(40,"JH",52.16) # Function  Call-
dispstuddata(50,"MB",24.86) # Function  Call-
print("-"*50)