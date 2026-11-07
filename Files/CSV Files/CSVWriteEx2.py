import csv
def AddRecordsToCSVFile():
    try:
        record=[5000,"aayush",6.5]

        with open("D:\\python\\Files\\CSV Files\\employee.csv","a",newline="") as fp:
            csvwobj=csv.writer(fp)
            print("record added to CSV file")
    except PermissionError:
        print("\t\tPermission Denied-TRY AGAIN")
AddRecordsToCSVFile()