class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance # this is the private varible

    def get_balance(self):
        return self.__balance
    
    def set_balance(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.set_balance(self.get_balance() + amount)

    def withdraw(self, amount):
        self.set_balance(self.get_balance() - amount)

    def __str__(self):
        return f"Owners name: {self.owner} \ncurrent balance: ${self.get_balance()}\n"
    
    def __add__(self,other):
        if isinstance(other, BankAccount):
            return BankAccount(f"{self.owner} and {other.owner}",self.get_balance() + other.get_balance())


class SavingsAccount(BankAccount):
    
    def withdraw(self, amount):
        if(self.get_balance() < amount):
            print("Insufficient balance")
        else:
            self.set_balance(self.get_balance() -  amount)

class CurrentAccount(BankAccount):
    
    def withdraw(self, amount):
        self.set_balance(self.get_balance() -  amount)

sa1 =  SavingsAccount('Jayesh',1000)
ca1 = CurrentAccount('Jayesh',100)

sa1.withdraw(2000)
ca1.withdraw(2000)

print(sa1)
print(ca1)