grade=int(input("enter your grade:"))
res="A" if grade>=90 else "B" if grade >=75 else "C" if grade>=55 else "D" if grade>=40 else "F"
print("grade {} is {}".format(grade,res))