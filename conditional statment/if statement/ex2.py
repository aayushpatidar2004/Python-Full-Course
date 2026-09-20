# program for accepting any value and
# Decide whether It is Palindrome or not

val = input("enter any value : ")
if (val==val[::-1]):
    print(" {} is  palindrome".format(val))
if (val!=val[::-1]):
    print(" {} is not palindrome".format(val))
print("end of the program")
    