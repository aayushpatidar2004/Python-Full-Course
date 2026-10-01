
#FunctionTestEx1.py
def welcome(name):  # Function Definition
    print("\t3-Line: Hi {}, Welcome to Functions Concept".format(name))
#-----------------------------------------------------
#Main Program
print("Type of welcome=",type(welcome))  #<class, function>
print("I am After Function Def and Before Fucntion Call")
welcome("ROSSUM")  # Function Call
welcome("TRAVIS") # Function Call
welcome("Hunter") # Function Call
print("I am from after Function Call")