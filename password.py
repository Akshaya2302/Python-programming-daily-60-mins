import string
import random
lower = string.ascii_lowercase
upper = string.ascii_uppercase
numbers = string.digits
symbols = string.punctuation

length = int(input("Enter the length of the password: "))
password = ""
for i in range(length):
    password += random.choice(lower + upper + numbers + symbols)
print(password) 