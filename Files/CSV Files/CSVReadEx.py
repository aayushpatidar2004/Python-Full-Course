import csv
def readcsvfiledata():
    try:
        with open("D:\\python\\Files\\CSV Files\\student.csv","r") as fp:
            csvrobj=csv.reader(fp)
            print("------------------CSV FILE DATA-------------------")
            for record in csvrobj:
                for val in record:
                    print("\t{}".format(val),end=" \t")
                print()
            print("---------------------------------------------------")
    except FileNotFoundError:
        print("\t\tCSV FILE NOT FOUND-TRY AGAIN")
readcsvfiledata()