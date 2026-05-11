import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) 
    for _ in range(length))
    return password

# Generate a few passwords
for i in range(5):
    print(generate_password(length=16))