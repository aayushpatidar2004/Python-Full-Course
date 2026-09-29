#Program for Validating the Name of Person / Product / Place
#NameValidationEx.py
while(True):
    name=input("Enter UR Name:")
    if(name.isspace()):
        print("\tDon't Enter Spaces for Ur Name-try again")
    else:
        words=name.split()
        if(len(words)==0):
            print("\tU Must Enter UR Name--try again")
        else:
            res=True
            for word in words:
                if(not word.isalpha()):
                    res=False
                    break
            if(res):
                print("\t'{}' is Valid Name".format(" ".join(words)))
                break
            else:
                print("\t'{}' is Invalid Name-try again".format(name))
