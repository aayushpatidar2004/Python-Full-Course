num=int(input("enter a number:"))
res="multiple of 10" if num%10==0 else "not a multiple of 10"
print("{} is {}".format(num,res))