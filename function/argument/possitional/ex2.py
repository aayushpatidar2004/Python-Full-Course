#Program for Demonstrating Possitional Arguments
#PossArgsEx2.py
def  dispstuddata(sno,sname,marks):
	print("\t{}\t{}\t{}".format(sno,sname,marks))

#Main Program
print("-"*50)
print("\tSNO\tNAME\tMARKS")
print("-"*50)
dispstuddata(10,"RS",34.56) # Function  Call--with Possitional Arguments
dispstuddata(20,"DR",54.16) # Function  Call--with Possitional Arguments
dispstuddata(30,"SR",34.86) # Function  Call--with Possitional Arguments
dispstuddata(40,"JH",52.16) # Function  Call--with Possitional Arguments
dispstuddata(50,"MB",24.86) # Function  Call-with Possitional Arguments
dispstuddata(marks=45.67,sno=60,sname="DT") # Function Call with Keyword Arguments
dispstuddata(70,marks=45.67,sname="PT") # Function  Call-with Possitional Arguments and Keyword Arguments
#dispstuddata(marks=45.67,sname="PT",70) # SyntaxError: positional argument follows keyword argument
print("-"*50)