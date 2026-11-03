import pickle
import sys

sys.path.append(r"D:\python\atmProject\case-3")

from NameValidation import validation
from NameExcept import InValidNameError, SpaceError, EmptyNameError
def addemp():
    try:
        print("---------------------------------------------------")
        empno=int(input("Enter Employee Number:"))
        empname=input("Enter employye name:")       
        empsal=input(("enter employye salary:"))    
        print("------------------------------------")
        lst=list()
        lst.append(empno)
        lst.append(empname)
        lst.append(empsal)
        with open ("Empolyee.data","ab") as fp:
            pickle.dump(lst,fp)
            print("Employee record saved successfully")
            print("---------------------------------------------")
    except valueError:
        print("\t\tDONT't ENTER ALNIMS,STRS AND SYMBOLS FOR EMPNO,SALARY")
    except InValidNameError:
        print("\tINVALID NAME-TRY AGAIN ")
    except SpaceError:
        print("\tDONT'T ENTER SPACE FOR NAME-TRY AGAIN")
    except EmptyNameError:
        print("\tU Must enter ur name --try again")
