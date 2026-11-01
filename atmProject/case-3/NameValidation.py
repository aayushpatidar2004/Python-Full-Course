#NameValidation.py<----Module Name
from NameExcept import InValidNameError,SpaceError,EmptyNameError
def  validation(name): #name= Guido Van3 Rossum
    if(name.isspace()):
        raise SpaceError
    else:
        words=name.split() #words=[Guido, Van3, Rossum]
        if(len(words)==0):
            raise EmptyNameError
        else:
            res=True
            for word in words:
                if(not word.isalpha()):
                    res=False
                    break
            if(res):
                return " ".join(words)
            else:
                raise InValidNameError