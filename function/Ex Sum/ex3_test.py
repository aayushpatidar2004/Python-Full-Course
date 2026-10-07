def welcome(name):
    print("\t3-Line: Hi {}, Welcome to Functions Concept".format(name))
#main Program
print("Type of welcome=",type(welcome))  #<class, function>
print("I am After Function Def and Before Function Call") 
welcome("ROSSUM")  # Function Call
welcome("TRAVIS") # Function Call
welcome("Hunter") # Function Call
print("I am from after Function Call")