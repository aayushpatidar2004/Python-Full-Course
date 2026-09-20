#Program for accepting any Numerical value and Decide whether It is +VE or -VE or Zero

val=float(input("enter any value : "))
if(val>0):
    print(" {} is  +ve".format(val))
if(val<0):
    print(" {} is -ve".format(val))
if(val==0):
    print(" {} is zero".format(val))
print("end of the program")