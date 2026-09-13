# Advanced Bitwise Operations in Python

num = 29

print("Number:", num)
print("Binary:", bin(num))

# Check whether a specific bit is ON or OFF
position = 3

if num & (1 << position):
    print("Bit", position, "is ON")
else:
    print("Bit", position, "is OFF")

# Set a bit
set_bit = num | (1 << 1)
print("After setting bit 1:", set_bit)

# Clear a bit
clear_bit = num & ~(1 << 2)
print("After clearing bit 2:", clear_bit)

# Toggle a bit
toggle_bit = num ^ (1 << 0)
print("After toggling bit 0:", toggle_bit)

# Count number of set bits (1s)
count = 0
temp = num

while temp:
    count += temp & 1
    temp >>= 1

print("Number of set bits:", count)

# Check if number is a power of 2
if num > 0 and (num & (num - 1)) == 0:
    print("Power of 2")
else:
    print("Not a power of 2")