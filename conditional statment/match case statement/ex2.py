s="""
    Area of Different Figures
    ________________
    C. Circle
    R. Rectangle
    S. Square  
    T. Triangle
    E. Exit
    ________________"""
print(s)
ch=input("Enter UR Choice:")
match(ch):
    case "C" |"c":
        r=float(input("Enter Radius :"))
        if(r<=0):
            print("Invalid Radius")
        else:
            ac=3.14*r*r
            print("Area of circle ",ac)
    case "R" |"r":
        l=float(input("Enter Length :"))
        b=float(input("Enter Breadth :"))
        if(l>0  and  b>=0):
            ar=l*b
            print("Area of Rectangle ",ar)
        else:
            if(l<=0):
                print("Invalid Length")
            if(b<=0):
                print("Invalid Breadth")
    case "S" |"s":
        side=float(input("Enter Side :"))
        sa=side*side
        print("Area of Square ",sa)
    case "T" |"t":
        b=float(input("Enter Base of triangle:"))
        h=float(input("Enter Height of triangle:"))
        if(h>0 and b>0):
            at=(1/2)*b*h
            print("Area of Triangle ",at)
        else:
            if(b<=0):
                print("Invalid Base")
            if(h<=0):
                print("Invalid Height")
    case "E" |"e":
        print("Thx for Using Program")
        exit() # Physical Termination / Exiting
    case _:
        print("UR Selection of Operation is Wrong-try again")
