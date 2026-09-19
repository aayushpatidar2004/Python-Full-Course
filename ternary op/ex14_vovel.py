a=input("enter a character:")
res="vowel" if a in "aeiouAEIOU" else "consonant"
print("{} is {}".format(a,res))