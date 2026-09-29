
#Program for accepting age of Citizen and Decide
# Whether Citizen is Eligible to Vote OR Not
#VoterEx1.py
age=int(input("Enter Age of Citizen: "))
if(age>=18):
    print("\t{} Years Citizen is Eligible to Vote".format(age))
else:
    print("\t{} Years Citizen is Not Eligible to Vote".format(age))