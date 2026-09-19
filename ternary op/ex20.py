temprature=float(input("enter temprature in celsius:"))
res="hot day " if temprature>30 else "cool day" if temprature>=20 and temprature<=30 else "cold day" 
print("{} is {}".format(temprature,res))