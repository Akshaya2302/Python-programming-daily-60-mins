class BankAccount:
    def __init__(self,balance=0):
        self.balance=balance
        
    def deposit(self,amount):
        self.balance+=amount
        print(f"Deposited: {amount}")
    def withdraw(self,amount):
        if amount>self.balance:
            print("Insufficient balance..")
        else:
            self.balance-=amount
            print(f"Withdrawn: {amount}")
    def display(self):
        print("Balance:",self.balance)
            

acc = BankAccount()

d=int(input("Enter the deposit amount:"))
acc.deposit(d)

w=int(input("Enter the amount to be withdrawn:"))
acc.withdraw(w)

acc.display()