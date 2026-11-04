import csv
def readcsvfiledata():
    with open("D:\\python\\Files\\CSV Files\\student.csv","r") as fp:
            csvdr=csv.DictReader(fp)
            for record in csvdr:
                for k in record:
                    print("\t{} -->{}".format(k,record.get(k))) 
                print("---------------------------------------------------")
readcsvfiledata()