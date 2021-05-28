def money(number):
    pattern = '${0:.2f}'
    return pattern.format(number)
    

class Account:
    def __init__(self, name, amount):
        self.owner = name
        self.balance = amount
        self.transactions = []
        self.runningBalance = amount
    def __str__(self):
        pattern = 'Account of {0}, balance: {1}'
        return pattern.format(self.owner, money(self.balance))
    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(['Deposit', amount])
    def withdraw(self, amount):
        self.balance -= amount
        self.transactions.append(['Withdrawal', amount])
    def statement(self):
        pattern = '{0:>12s} {1:>12s} {2:>12s}'
        print(pattern.format('Withdrawals', 'Deposits', 'Balance'))
        print(pattern.format('','', money(self.runningBalance)))
        for transaction in self.transactions:
            amount = transaction[1]
            if transaction[0] == 'Deposit':
                self.runningBalance += amount
                print(pattern.format('', money(amount), money(self.runningBalance)))
            else:
                self.runningBalance -= amount
                print(pattern.format(money(amount), '', money(self.runningBalance)))
        self.transactions = []   


x = Account('John Doe', 321)

print(x)
print()

x.deposit(1.95)
x.withdraw(22.95)
x.withdraw(100)
x.statement()

print()
print()

x.deposit(300)
x.withdraw(29.95)
x.withdraw(75.92)
x.statement()
