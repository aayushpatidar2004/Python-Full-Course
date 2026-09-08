
#program acceping Any Two Numerical Integer Values and Swap Them OR Interchange them--Logic-3
#ArithmeticOperatorsEx5.py
a=int(input("Enter the First Value:"))
b=int(input("Enter the Second Value:"))
print("-"*40)
print("Original Values")
print("-"*40)
print("\tOriginal Value of a=",a)
print("\tOriginal Value of b=",b)
print("-"*40)
#Swapping Logic--Single Line assginment
a=a+b
b=a-b
a=a-b
print("\tSwapped  Value of a=",a)
print("\tSwapped Value of b=",b)
