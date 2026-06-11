users = {}
contacts = {}

user_name = input("Create username:")
password = input("Create Password:")

users[user_name] = password

u = input("Enter the username:")
p = input("Enter the password:")

if users.get(u) == p:
    print("Logged in Successfully...!")
    
    while True:
        print("\n 1.Add 2.View 3.Delete 4.Show all 5.Exit")
        
        choice = int(input("Enter your choice:"))
        if choice == 1:
            name = input("Enter your name:")
            contact = input("Enter your contact details:")
            contacts[name] = contact
            
        elif choice == 2:
            name = input("Enter name:")
            print(contacts.get(name, "Not found"))
            
        elif choice == 3:
            name = input("Enter name:")
            if name in contacts:
                del contacts[name]
                print("Contact deleted!")
            else:
                print("Contact not found!")
            
        elif choice == 4:
            print(contacts)
            
        elif choice == 5:
            print("Exiting...")
            break
        else:
            print("Invalid choice!")
            
else:
    print("Invalid Login")