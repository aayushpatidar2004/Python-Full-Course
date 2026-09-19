char1=input("enter a character:")
res ="upeercase" if char1>='A' and char1<='Z' else "lowercase" if char1>='a' and char1<='z' else "not a character"
print("{} is {}".format(char1,res))