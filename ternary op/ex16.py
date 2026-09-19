num=float(input("Enter a number: "))
res="single digit"if num>=0 and num<=9 else "double digit" if num>=10 and num<=99 else "triple digit" if num>=100 and num<=999 else "more than 3 digits"
print("{} is {}".format(num,res))