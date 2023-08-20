class User:
    #below is the constructor 
    def __init__ (self, name):
        self.name = name
    def greet(self):
        print(f"Hello {self.name}")
        
        
me = User("Alan")

me.greet()


class BankAccount:
    def __init__(self, account_type):
        self.type = account_type
        self.balance = 0

    def withdraw(self, amount):
        self.balance -= amount
        return amount

    def deposit(self, amount):
        self.balance += amount
        return self.balance

checking = BankAccount('checking')
savings = BankAccount('savings')

savings.deposit(1000)
transfer = savings.withdraw(500)
checking.deposit(transfer)



        
        

        









        