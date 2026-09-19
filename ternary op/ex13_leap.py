year=int(input("enter a year:"))
res="leap year" if  ((year %4 ==0) and (year%100!=0) or (year%400==0) )else "not leap year"    
print("{} is {}".format(year,res))