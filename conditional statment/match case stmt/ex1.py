#program for Implementaing Arithmetic Operations By using Match Case
#MatchCaseEx1.py
print("="*50)
print("\tArithmetic Operations")
print("="*50)
print("\t\t1.Addition")
print("\t\t2.Subtraction")
print("\t\t3.Multiplication")
print("\t\t4.Division")
print("\t\t5.Modulo Division")
print("\t\t6.Exponentiation")
print("\t\t7.Exit")
print("="*50)
ch=int(input("Enter UR Choice:"))
match(ch):
    case 1:
        print("Enter Two Numbers for Addition")
        a,b=float(input()),float(input())
        print("\tSum({},{})={}".format(a,b,a+b))
    case 2:
        print("Enter Two Numbers for Substraction")
        a, b = float(input()), float(input())
        print("\tSub({},{})={}".format(a, b, a - b))
    case 3:
        print("Enter Two Numbers for Multiplication")
        a, b = float(input()), float(input())
        print("\tMul({},{})={}".format(a, b, a * b))
    case 4:
        print("Enter Two Numbers for Division")
        a, b = float(input()), float(input())
        print("\tDiv({},{})={}".format(a, b, a / b))
        print("\tFloorDiv({},{})={}".format(a, b, a // b))
    case 5:
        print("Enter Two Numbers for Division")
        a, b = float(input()), float(input())
        print("\tModDiv({},{})={}".format(a, b, a % b))
    case 6:
        a, b = float(input("Enter Base:")), float(input("Enter Power:"))
        print("\tPow({},{})={}".format(a, b, a ** b))
    case 7:
        print("Thx for Using Program")
        exit() # Physical Termination / Exiting
    case _:
        print("UR Selection of Operation is Wrong-try again")
print("Program Execution Completed")