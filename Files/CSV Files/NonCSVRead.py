#Program for Reading the Records from CSV File--
#Non-CSVReadEx.py
with open("D:\\python\\Files\\CSV Files\\student.csv","r") as fp:
    csvfiledata=fp.read()
    print(csvfiledata)
