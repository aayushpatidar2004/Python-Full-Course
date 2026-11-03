#EmpSearch.py<-------Module Name
import pickle

def searchemp():
    # Get all the Records from File
    records = []  # Empty list for adding the records--each record ins one list--List in list
    with open("Employee.data", "rb") as fp:
        while (True):
            try:
                record = pickle.load(fp)
                records.append(record)
            except EOFError:
                break
    # Get the Employee Number to view Other Details
    res = False  # Employee Record Not Found
    empno = int(input("\tEnter Employee Number to View Details:"))
    for ind in range(len(records)):
        if (records[ind][0] == empno):
            recindx=ind
            res = True  # Employee Record  Found
            break
    print("------------------------------------------")
    print("\tValid Employee--Employee Found" if res else "\t\tInvalid Employee--Employee Not Found")
    print("------------------------------------------")