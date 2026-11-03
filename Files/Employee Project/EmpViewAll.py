
import pickle
def viewallemployees():
    try:
        with open("Employee.data","rb") as fp:
            print("-----------------------------------------")
            print("\tEMPNO\tNAME\tSALARY")
            print("-----------------------------------------")
            while(True):
                try:
                    record = pickle.load(fp)
                    for val in record:
                        print("\t{}".format(val),end="\t")
                    print()
                except EOFError:
                    print("-----------------------------------------")
                    break
    except FileNotFoundError:
        print("Employee File Does Not Exist")