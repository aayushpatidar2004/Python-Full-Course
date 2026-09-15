# first_name ="tony"
# last_name="stark"
# age=53
# height=1.85

# superhero=input("enter superhero name:")
# print("First name",first_name)
# print("second name",last_name)
# print("age",age)
# print("height",height)
# print("superhero name",superhero)

# ******************************************************

# RANDOM PASSWORD GENERATOR
import random
import string

pass_len=8
charvalues= string.ascii_letters + string.digits + string.punctuation
password = " "
for i in range(pass_len):
    password += random.choice(charvalues)

print("your passworld :", password)


