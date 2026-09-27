
#Program for Finding Sum of Digits of a +ve Number
#SumsDigisSumEx1.py
num=int(input("Enter Any Number:"))
if(num<=0):
    print("\t{} is Invalid Input".format(num))
else:
    s=0
    for d in str(num):
        s=s+int(d)
    else:
        print("Sum_of_digits({})={}".format(num,s))
