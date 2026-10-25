#program for Reading the values from Key Board By using List Comprehension
#ListCompEx2.py
print("Enter List of Numerical Values Separated by Comma:")
lst=[ float(val)  for val in input().split(",")  ]  # List Comprehension
print("List of Values=",lst)

