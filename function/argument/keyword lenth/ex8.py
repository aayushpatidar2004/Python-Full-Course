#Program for Cal total marks of those students who are studying Different Classes and who secured different Marks in Different Subjects.
#PureKeywordVariableLengthArgsEx5.py
def  findTotalMarks(sno,sname,cls,*intmarks,crs="PYTHON",city="HYD",**submarks):
	print("*"*50)
	print("\tStudent Number=",sno)
	print("\tStudent Name=",sname)
	print("\tStudent Class=",cls)
	print("\tStudent Course=",crs)
	print("\tStudent City=",city)
	if(len(intmarks)!=0):
		print("\tStudent Internal Marks=",intmarks)
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
findTotalMarks(10,"Ambar","X", 10,15,16,12,11,17,telugu=90,hindi=91,english=89,maths=99,sci=93,soc=96)
findTotalMarks(20,"Omkar","XII", 1.2,2.3,4.5,5.6,3.4,Sanskrit=99,English=89,Maths=75,Phy=60,Che=58)
findTotalMarks(30,"Dinesh","B.Tech",20,21,25,23,OS=50,DBMS=65,CNN=55,JavaLab=30)
findTotalMarks(40,"Trump","Politics",city="USA",Eco=70,Civics=50,crs="HTML")
findTotalMarks(50,"Rossum","Research",1.2,6.7,7.8,city="NL")