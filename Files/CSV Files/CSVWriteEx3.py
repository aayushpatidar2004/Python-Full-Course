#program for Creating a CSV File
#CSVWriteEx3.py
import csv
def createCSVFilewithDict():
    colnames=["TNO","NAME","SUB"] #Step-1 #Step-1
    records=[{"TNO":100,"NAME":"Rajesh","SUB":"PYTHON"},
            {"TNO": 200, "NAME": "Rakesh", "SUB": "JAVA"},
            {"TNO":300,"NAME":"Ramesh","SUB":"C"},
            {"TNO":400,"NAME":"Raj","SUB":"DSA"}]#Step-2
    with open("D:\\python\\Files\\CSV Files\\teacher.csv","w",newline="") as fp: #Step-3
        csvdwr=csv.DictWriter(fp, fieldnames=colnames)  #Step-4--here csvdwr is an object <class, csv.DictWriter>
        #Here csvdwr object contains 3 Functions   1) writeheader()   2) writerows()   3) writerow()
        csvdwr.writeheader() #Step-5
        csvdwr.writerows(records) #Step-6
        print("CSV File Created with Collection of Records--verify")

#Main Program
createCSVFilewithDict()