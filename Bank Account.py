class BankAccount:
    account_name="uma"
    account_number="12345"
    balance=100000
    
    def deposit(self):
        money=int(input("Enter the money:"))
        money=money+self.balance
        print(money)
    def withdraw(self):
        cash=int(input("Enter cash: "))
        print(cash)
    def display(self):
        print(self.balance)
a=BankAccount()
a.deposit()
a.withdraw()
a.display()