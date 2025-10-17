#shared veriable
#state dependent balance is the state

balance = 100 #global variable common in betn all functions

def deposit(amount):
    global balance
    balance += amount

def withdraw(amount):
    global balance
    balance -= amount

deposit(50)
deposit(50)
withdraw(20)
print(balance)

#procedural approch not state dependent

# def deposit(balance, amount):
#     # global balance
#     balance += amount

# def withdraw(balance, amount):
#     # global balance
#     balance -= amount

