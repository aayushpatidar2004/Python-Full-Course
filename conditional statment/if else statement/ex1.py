
#program for accepting any value and Decide whether It is Palindrome or not
val=input("enter any number :")
if(val==val[::-1]):
    (print("\t {} is palindrome ".format(val)))
else:
    print("\t {} is not palindrome ".format(val))
print("thank you for using this program")