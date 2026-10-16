ch = input("Enter a character: ").strip()

if len(ch) != 1:
    print("Please enter exactly one character")
elif ch.isupper():
    print("Uppercase")
elif ch.islower():
    print("Lowercase")
elif ch.isdigit():
    print("Digit")
else:
    print("Special Character")