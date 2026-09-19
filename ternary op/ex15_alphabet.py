ch=input("enter a character:")
res="alphabet" if ('A'<=ch and ch<='Z') or ('a'<=ch and ch<='z') else "not alphabet"
print("{} is {}".format(ch,res))