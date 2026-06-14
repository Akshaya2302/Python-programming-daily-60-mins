while True:
    print("Who Are You?")
    name = input("Name:") # Adding a prompt helps!
    if name != "Joe":
        continue
    print("Helloo JOE....")
    password = input("Passowrd:") # Now you'll know it's waiting for the password
    if password == "1234":
        break
print("Access Granted!")