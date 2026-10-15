
#Program for Demonstrating the Need of  Keyword Variable Length Arguments
#In This we have Family Similar Function Calls and we have corresponding Multiple  Functions Def with same Function Name. This Program will not execute as it is bcoz PVM Performs Interpretation Process and Remembers Only Latest Function Definition  But not all.
#KeywordVariableLengthArgsEx2.py
def disp(sno,sname,mm,em,cname): # Function Def-1
	print(sno,sname,mm,em,cname)
def disp(tno,tname,sub1,sub2):  # Function Def-2
	print(tno,tname,sub1,sub2)
def disp(cid,cname,hb):  # Function Def-3
	print(cid,cname,hb)

#Main Program
disp(sno=10,sname="RS",mm=56,em=70,cname="PSF") # Function Call-1 with 5 Keyword Arguments
disp(tno=100,tname="TR",sub1="PYTHON",sub2="Numpy")# Function Call-2 with 4 Keyword Arguments
disp(cid=1000,cname="JH",hb="Drawing") # Function Call-3 with 3 Keyword Arguments