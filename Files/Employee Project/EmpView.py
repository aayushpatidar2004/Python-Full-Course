import pickle
def viewsingleemp():
    records=[]
    with open("Employee.data","rb") as fp:
        while (True):
            try:
                record=pickle.load(fp)
                records.append(record)
            except EOFError:
                break
    res=False
    empno=int(input("Enter Employee Number to view:"))
    for ind in range(len(records)):
        if (records[ind][0]==empno):
            recorddet=records[ind]
            res=True
            break
    print("-------------------------------------")
    if (res):
        print("\t Employee Details")
        print("------------------------------------")
        print("\t\tEmployee Number: {}".format(recorddet[0]))
        print("\t\tEmployee Name: {}".format(recorddet[1]))
        print("\t\tEmployee Salary: {}".format(recorddet[2]))
    else:
        print("\t\tEmployee Record Not Found")
        print("-------------------------------------")
