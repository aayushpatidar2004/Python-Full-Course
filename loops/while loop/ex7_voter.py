#Program for accepting age of Citizen and Decide
# Whether Citizen is Eligible to Vote OR Not
#VoterEx2.py
while(True):
    age=int(input("\tEnter Age of Citizen: "))
    if(age>=18):
        print("\t{} Years Citizen is Eligible to Vote".format(age))
        break
    else:
        print("\t{} Years Citizen is Not Eligible to Vote".format(age))
print("Loop Execution Completed ")