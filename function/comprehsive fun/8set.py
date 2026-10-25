#Program for Getting all Even Numbers By using Set Comprehension
#ListCompEx1.py
lst=[10,13,14,15,16,17,31,32]
el={val  for val in lst  if val%2==0}  # Set Comprehension
ol={val for val in lst if val%2!=0} # Set Comprehension
print("Even Numbers=",el)
print("Odd Numbers=",ol)
