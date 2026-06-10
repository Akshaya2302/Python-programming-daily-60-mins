password=input("Enter the password: ")

if (len(password)>=6 and any(ch.isupper()for ch in password)and any(ch.islower()for ch in password) and any(ch.isdigit()for ch in password)):
    print("valid PAssword")
else:
    print("Invalid password..")
    
text=input("Enter the text:")
text_only=""

for ch in text:
    if ch.isalnum() or ch.isspace():
        text_only+=ch
        
print("formatted text:",text_only)
