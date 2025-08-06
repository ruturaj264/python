class Account():

    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

    def deposit(self, depositAmount):
        self.amount += depositAmount
        print('Deposit Accepted!!')

    def withdraw(self, withdrawAmount):
        if withdrawAmount > self.amount:
            print('Withdraw Rejected!!')
        else:
            self.amount -= withdrawAmount
            print('Withdraw Accepted!!')

    def __str__(self):
        return f'Name : {self.name} Amount : {self.amount}'
    
account1 = Account('Ram', 500)

print(account1.amount)
account1.deposit(200)
account1.deposit(200)
print(account1.amount)

account1.withdraw(500)
print(account1.amount)

