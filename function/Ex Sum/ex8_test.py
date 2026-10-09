#Functions for Finding Length of words in a Line fo Text
#WordsLengthInLine.py
def readLine():
    return input("Enter a Line of Text:")

def findwordlength():
    line=readLine() #Function Chaining-- line=Python is an oop lang
    print("------------------------------------------")
    words=line.split() #words=[Python, is, an, oop,lang]
    for word in words:
        print("\t{}-->{}".format(word,len(word)))
    print("------------------------------------------")


#Main Program
findwordlength()