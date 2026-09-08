#Program for Demonstrating Arithmetic Operations
#ArithmeticOperatorsEx2.py
a,b=float(input("Enter the First Value:")),float(input("Enter the Second Value:"))
ap,sp,mp,dp,fd,md,ep=a+b,a-b,a*b,a/b,a//b,a%b,a**b
print("="*50)
print("\tResults of Arithmetic Operators")
print("="*50)
print("\tSum({},{})={}".format(a,b,ap))
print("\tSub({},{})={}".format(a,b,sp))
print("\tMul({},{})={}".format(a,b,mp))
print("\tDiv({},{})={}".format(a,b,dp))
print("\tFloorDiv({},{})={}".format(a,b,fd))
print("\tModDiv({},{})={}".format(a,b,md))
print('\tPow({},{})={}'.format(a,b,ep))
print