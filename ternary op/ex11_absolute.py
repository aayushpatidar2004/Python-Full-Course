num = int(input("Enter a number: "))

result = num if num >= 0 else -num

print("Absolute value of {} is {}".format(num, result))