import csv
def dynamiccsvfilecreate():
    noc= int (input("Enter the Number of Columns:"))
    if (noc<=0):
        print("\t\tINVALID NUMBER OF COLUMNS-TRY AGAIN")
    else:
        colnames=[]
        for i in range(1,noc+1):
            col=input("Enter {} Column Name:".format(i))
            colnames.append(col)
        else:
            nor= int (input("Enter the Number of Records:"))
            if (nor<=0):
                print("\t\tINVALID NUMBER OF RECORDS-TRY AGAIN")
            else:
                records=list()
                for i in range(1,nor+1):
                    print("----------------------------")
                    record=list()
                    for cn in colnames:
                        cval=input("Enter {} Value:".format(cn))
                        record.append(cval)
                    print("----------------------------")
                    records.append(record)
                else:
                    while True:
                        fname=input("Enter the CSV File Name with Path:")
                        if (fname.endswith(".csv")):
                            break
                        else:
                            print("\t\tINVALID CSV FILE NAME-TRY AGAIN")
                    with open("D:\\python\\Files\\CSV Files\\" + fname, "a",newline="") as fp:
                                csvwobj=csv.writer(fp)
                                csvwobj.writerow(colnames)
                                csvwobj.writerows(records)
                                print("\t\tCSV FILE CREATED SUCCESSFULLY")
                                
dynamiccsvfilecreate()