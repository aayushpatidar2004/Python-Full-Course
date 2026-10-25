#program for Reading Only +VE values from Key Board By using List Comprehension
#ListCompEx4.py
lst=[ float(val)  for val in input("Enter List of Numerical Values Separated by Comma:\n").split(",") if float(val)>=0 ]  # List Comprehension
print("List of +VE Values=",lst)

