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
        # self._balance = self._balance - amount
        self.set_balance(self.get_balance() - amount)

    def __str__(self):
        return f"Owners name: {self.owner} \ncurrent balance: ${self.get_balance()}\n"
    
    def __add__(self,other):
        if isinstance(other, BankAccount):
            return BankAccount(f"{self.owner} and {other.owner}",self.get_balance() + other.get_balance())
        

Account1 =  BankAccount('Jayesh', 1000)
Account2 =  BankAccount('Shruti', 2000)

print("", Account1)

Account1.deposit(1000)
print("", Account1)

Account2.withdraw(500)
print("", Account2)

Account3 = Account1 + Account2  #this will call __add__ if not implemented will cause an error
print("", Account3)
