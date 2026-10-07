def readn():
    n =int(input("Enter a number:"))
    return n
def multable():
    n=readn()
    if(n<=0):
        print("Please enter a positive number")
    else:
        print("Multiplication Table of {}".format(n))
        for i in range(1,11):
            print("{} x {} = {}".format(n,i,n*i))
multable()