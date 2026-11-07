import csv
def createCSVFile():
    colnames=["ENO","NAME","SAL"]
    
    records=[[101,"Ravi",10000],
            [102,"Ramesh",20000],
            [103,"Suresh",30000],
            [104,"Mahesh",40000],
            [105,"Naresh",50000]]
    with open("D:\\python\\Files\\CSV Files\\employee.csv","w",newline="") as fp:
        csvwr=csv.writer(fp)
        csvwr.writerow(colnames)
        csvwr.writerows(records)
        print("CSV File Created Successfully")
createCSVFile()