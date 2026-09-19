cgpa=float(input("enter your cgpa:"))
res="eligible" if (cgpa>=9.5) and(cgpa<=10) else "not eligible"
print("{} cgpa student is {}".format(cgpa,res))