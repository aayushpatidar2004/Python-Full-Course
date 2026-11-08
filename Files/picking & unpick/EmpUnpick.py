import pickle
def readrecords():
    with open("emp.data","rb") as fp:
        print("----------------------------------")
        while(True):
            try:
                record=pickle.load(fp)
                for val in record:
                    print("\t{}".format(val),end="\t")
                print()
            except EOFError:
                print("----------------------------")
                break
readrecords()