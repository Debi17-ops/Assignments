class BankAccount:
    def __init__(self,account_number,account_holder,balance=0.0):
        self.account_number=account_number
        self.account_holder=account_holder
        self.balance=balance
    
    def deposit(self,amount):
        self.balance += amount
        print(f"Deposited {amount}\nNew balance is{self.balance}")
        
    def withdraw(self,amount):

        if amount<=self.balance:
            self.balance -=amount
            print(f"withdrew {amount}\nNew balance is {self.balance}")
        else:
            print("insufficient balance")
    
    def get_balance(self):
        return self.balance


account= BankAccount("12345678","Debi",100000.0)
account.deposit(int(input("enter the deposit amount:")))
account.withdraw(int(input("enter the withdrawal amount:")))
print(f"Current balance:{account.get_balance()}")
