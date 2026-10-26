a=10
b=20
def operation():
    k=globals()
    print("implicit and programmer defined global variables ")
    for key, value in k.items():
        print("\t\t{}={}".format(key,value))
    print("-"*50)
    print("progrmmer defined globals variables way 1")
    print("\tglobal var a={}".format(k.get('a')))
    print("\tglobal var b={}".format(k.get('b')))
    print("-"*50)
    print("progrmmer defined globals variables way 2")
    print("\t global var a={}".format(k['a']))
    print("\t global var b={}".format(k['b']))
    print("-"*50)
    print("Programmer-Defined Global Variables--Way-3")
    print("\tGlobal Var a={}".format(globals().get('a')))
    print("\tGlobal Var b={}".format(globals().get('b')))
    print("-"*50)
    print("Programmer-Defined Global Variables--Way-4")
    print("-"*50)
    print("\tGlobal Var a={}".format(globals()['a']))
    print("\tGlobal Var b={}".format(globals()['b']))
    print("-"*50)
#Main Program
operation()
