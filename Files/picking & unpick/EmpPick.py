import pickle
def saveempdata():
    with open("emp.data","ab") as fp:
        while(True):
            print("-----------------------------------------")
            empno=int(input("Enter Employee Number:"))
            empname=input("Enter employye name:")
            empsal=input(("enter employye salary:"))
            print("----------------------------------------------")
            #Create an empty list object
            lst=list()
            lst.append(empno)
            lst.append(empname)
            lst.append(empsal)
            #save Iterable Object-lst into into the file
            pickle.dump(lst,fp)
            print("employee recored saved in files:")
            print("--------------------------------------------")
        
            ch=input("do you want save another record(yes/no):")
            if(ch.lower()=="no"):
                print("thx for using program")
                break
saveempdata()