num=float(input("Enter a number: "))
res="divisible by both 3 and 5" if num%3==0 and num%5==0 else "not divisible by both 3 and 5"
print("{} is {}".format(num,res))