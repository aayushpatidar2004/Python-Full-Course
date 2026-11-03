#EmpDelete<-----------Module Name
import pickle
def deleteemp():
    #Get all the Records from File
    records = []  # Empty list for adding the records--each record ins one list--List in list
    with open("Employee.data", "rb") as fp:
        while (True):
            try:
                record = pickle.load(fp)
                records.append(record)
            except EOFError:
                break
    #Accept the employee Number to delete employee record
    res=False
    empno=int(input("\tEnter Employee Number to Delete:"))
    for index in range(len(records)):
        if(records[index][0]==empno):
            res=True
            recind=index
            break
    print("-----------------------------------------------------")
    if(res):
        records.pop(recind)
        #Re-write the remaining records in File
        with open("Employee.data", "wb") as fp:
            for record in records:
                pickle.dump(record, fp)
        print("\t\tEmployee Record Deleted--verify")
    else:
        print("\t\tEmployee Record Not Found")
    print("-----------------------------------------------------")
