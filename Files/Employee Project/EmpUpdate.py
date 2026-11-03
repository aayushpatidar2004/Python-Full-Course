import pickle
def updateemp():
    records=[]
    with open("Employee.data","rb") as fp:
        while (True):
            try:
                record=pickle.load(fp)
                records.append(record)
            except EOFError:
                break
    
    empno=int(input("Enter Employee Number to update salary:"))
    
    res=False
    for ind in range(len(records)):
        if (records[ind][0]==empno):
            recind=ind
            res=True
            break
    print("-------------------------------------")
    if (res):
        newsal=float(input("\t\tEnter new salary for employee: "))
        records[recind][2]=newsal
        with open("Employee.data","wb") as fp:
            for record in records:
                pickle.dump(record,fp)
            print("\t\tEmployee Record Updated Successfully")
    else:
        print("\t\tEmployee Record Not Found")
    print("-------------------------------------")