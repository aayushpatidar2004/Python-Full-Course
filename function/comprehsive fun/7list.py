#Program for Reading List of Words whose Length Ranges Between 3 and 4 (Inclusive)
print("Enter List of Words Separated Comma:")
words=[ val  for val in input().split(",") if len(val) in range(3,5) ]
print("List of Words=",words)