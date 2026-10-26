#Program for Demonstrating globals()
#In this Program we have SAME NAMES for Global and Local Variables
#GlobalsFunEx2.py
a=10
b=20
c=30
d=40  # Here a,b,c,d are Called Global Varaibles
def operation():
	a=100
	b=200
	c=300
	d=400  # Here a,b,c,d are Called Local Variables
	res=a+b+c+d+ globals()['a'] +globals()['b'] + globals().get('c') +globals().get('d')
	print("Result=",res)
#Main Program
operation()
