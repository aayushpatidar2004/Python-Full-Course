#Program for Demonstrating Keyword Arguments
#KeywordArgsEx1.py
def disp(a,b,c,d):
	print("\t{}\t{}\t{}\t{}".format(a,b,c,d))

#Main Program
print("-"*50)
print("\tA\tB\tC\tD")
print("-"*50)
disp(10,20,30,40) # Function Call with Possitional Arguments
disp(c=30,d=40,b=20,a=10) # Function Call with Key Arguments
disp(b=20,a=10,d=40,c=30)  # Function Call with Key Arguments
#disp(10,c=30,b=20,40)---SyntaxError: positional argument follows keyword argument
disp(10,c=30,b=20,d=40)
