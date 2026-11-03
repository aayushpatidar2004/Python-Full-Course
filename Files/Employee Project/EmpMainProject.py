#EmpMainProject.py<------Main Program
from EmpMenu import menu
from EmpAdd import addemp
from EmpViewAll import viewallemployees
from EmpView import viewsingleemp
from EmpUpdate import updateemp
from EmpDelete import deleteemp
from EmpSearch import searchemp
while(True):
    try:
        menu()
        ch=int(input("Enter UR Choice: "))
        match(ch):
            case 1:
                addemp()
            case 2:
                deleteemp()
            case 3:
                updateemp()
            case 4:
                viewsingleemp()
            case 5:
                viewallemployees()
            case 6:
                searchemp()
            case 7:
                print("\tTHX FOR USING PROJECT")
                break
            case _: #Default case block
                print("\tUR SELECTION OF CHOICE IS WRONG-TRY AGAIN")
    except ValueError:
        print("\t\tDON'T ENTER ALNUMS,STRS AND SYMBOLS-TRY AGAIN")
