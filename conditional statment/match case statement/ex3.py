s="""=====================================================
	Area of Different Figures
=====================================================
        C. Circle
        R. Rectangle				
        S. Square		
        T. Triangle
        E. Exit
====================================================="""
print(s)
ch=input("Enter UR Choice:")
match(ch.upper()):
    case "C":
        r=float(input("Enter Radius:"))
        if(r<=0):
            print("Invalid Radius")
        else:
            ac=3.14*r**2
            print("Area of Circle:",ac)
    case "R":
        L=float(input("Enter Length:"))
        B=float(input("Enter Breadth:"))
        if(L>0) and (B>0):
            ar=L*B
            print("Area of Rectangle:",ar)
        else:
            if(L<=0):
                print("Invalid Length")
            if(B<=0):
                print("Invalid Breadth")
    case "S":
        side=float(input("Enter Side Value of Square:"))
        sa=side*side
        print("Area of Square:",sa)
    case "T"|"t":
        b=float(input("Enter Base Value of Triangle:"))
        h=float(input("Enter Height Value of Triangle:"))
        if (h > 0) and (b > 0):
            at=(1/2)*h*b
            print("Area of Triangle:",at)
        else:
            if (b <= 0):
                print("Invalid Base")
            if (h <= 0):
                print("Invalid Height")
    case "E":
        print("Thx for Using Program")
        exit()
    case _:  # default block
        print("UR Selection of Operation is Wrong--Try again")
