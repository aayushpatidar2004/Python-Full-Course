
#Program for Demonstrating the Concept of Variable Length Arguments
#PureVariableLengthArgsEx4.py
def disp(sno,sname,marks,*vals,crs="PYTHON"):
	print("\tStudent Number:",sno)
	print("\tStudent Name:",sname)
	print("\tStudent Marks:",marks)
	print("\tStudent Course:",crs)
	print("\tVariabel Length Values={}   Sum={}".format(vals,sum(vals)))
	print("-----------------------------------------------------------------------------------------")

#Main Program
disp(100,"RS",34.56,10,20,30,40,50)  # Function Call with  5  Positional Args
disp(200,"TR",22.22,10,20,30,40)		# Function Call with  4  Positional Args
disp(300,"DR",66.66,10,20,30)		# Function Call with  3  Positional Args
disp(400,"JH",33.23,10,20)		# Function Call with  2  Positional Args
disp(500,"MB",66.12,10)		# Function Call with  1  Positional Args
disp(600,"DT",11.11)       # Function Call with 