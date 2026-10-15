#Program for Cal total marks of those students who are studying Different Classes and who secured different Marks in Different Subjects.
#PureKeywordVariableLengthArgsEx4.py
def  findTotalMarks(sno,sname,cls,crs="PYTHON",city="HYD",**submarks):
	print("*"*50)
	print("\tStudent Number=",sno)
	print("\tStudent Name=",sname)
	print("\tStudent Class=",cls)
	print("\tStudent Course=",crs)
	print("\tStudent City=",city)
	if(len(submarks)!=0):
		totmarks=0
		print("---------------------------------------------------------")
		print("\tSubject\t\tMarks")
		print("---------------------------------------------------------")
		for subject,marks in submarks.items():
			print("\t{}\t\t{}".format(subject,marks))
			totmarks=totmarks+marks
		print("\tTOTAL MARKS=",totmarks)
	print("*"*50)

#Main Program
findTotalMarks(10,"Ambar","X", telugu=90,hindi=91,english=89,maths=99,sci=93,soc=96)
findTotalMarks(20,"Omkar","XII", Sanskrit=99,English=89,Maths=75,Phy=60,Che=58)
findTotalMarks(30,"Dinesh","B.Tech",OS=50,DBMS=65,CNN=55,JavaLab=30)
findTotalMarks(40,"Trump","Politics",city="USA",Eco=70,Civics=50,crs="HTML")
findTotalMarks(50,"Rossum","Research",city="NL")