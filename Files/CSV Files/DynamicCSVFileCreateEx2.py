#Program for Creating Dynamic CSV File By Reading Col Names and Records from KBD
#DynamicCSVFileCreateEx2.py
import csv
def dynamiccsvfilecreate():
    noc=int(input("Enter How Many Col Names u Have:"))
    if (noc<=0):
        print("\tInvalid Number of Columns--try again")
    else:
        colnames=[]  # empty List for adding column names
        for i in range(1,noc+1):
            col=input("Enter {} Column Name:".format(i) )
            colnames.append(col)
        else:
            #Get the records from KBD
            nor=int(input("Enter How Many Records u Have:"))
            if(nor<=0):
                print("\tInvalid Number of Records--try again")
            else:
                records=list()  # Outer List for adding records(inner list)
                for i in range(1,nor+1):
                    print("--------------------------------------------")
                    print("\tEnter {} Record Deatils".format(i) )
                    print("--------------------------------------------")
                    record= {} # Inner Dict--for adding Single Record (Key,Value)
                    for cn in colnames:
                        cval=input("Enter Value for {}:".format(cn))
                        record[cn]=cval
                    print("--------------------------------------------")
                    records.append(record)
                else:
                    #Choose the csv file name
                    while(True):
                        filename=input("Enter CSV File Name with an extension .csv")
                        if(filename.endswith(".csv")):
                            break
                        else:
                            print("\tInvalid File Extension--try again")
                    #open in CSV File Name in write mode
                    with open("D:\\python\\Files\\CSV Files\\"+filename,"a",newline="") as fp:
                        csvwr=csv.DictWriter(fp,fieldnames=colnames)
                        csvwr.writeheader()
                        csvwr.writerows(records)
                        print("CSV File Created Dynamically-Verify")

#Main Program
dynamiccsvfilecreate()
