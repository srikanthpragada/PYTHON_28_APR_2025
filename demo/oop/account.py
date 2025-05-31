class Account:
    # Class attribute or Static Attribute
    minbalance = 10000

    def __init__(self, acno, customer, balance=0):
        # Object attributes
        self.acno = acno
        self.customer = customer
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError('Invalid Amount. It must be > 0')

        self.balance += amount

    def withdraw(self, amount):
        if self.balance - Account.minbalance >= amount:
            self.balance -= amount
        else:
            raise ValueError("Insufficient Balance!")

    def getbalance(self):
        return self.balance

    @staticmethod
    def getminbalance():
        return Account.minbalance

print(Account.getminbalance())

a = Account(1, "Jack", 10000)
a.deposit(1000)
a.withdraw(30000)
print(a.getbalance())

b = Account(2, "Mark")
b.balance = 100000
print(b.balance)


accounts = []
sorted(accounts, key = lambda a : a.balance)
