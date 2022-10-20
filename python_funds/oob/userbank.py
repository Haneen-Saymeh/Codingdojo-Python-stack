class Account:
    def __init__(self, int_rate=.01, balance=0):
        self.balance=balance
        self.int_rate = int_rate


    def deposit(self, amount):
        self.balance += amount
        
    def withdraw(self, amount):
        if amount>self.balance:
            self.balance=self.balance- 5
            print("Insufficient funds: Charging a $5 fee")
        else:
            self.balance = self.balance-amount
        
    def display_account_info(self):

        print("Balance:",self.balance)

    def yield_interest(self):
        if self.balance >0:
            self.balance = (self.int_rate*self.balance)+self.balance


# acount1= Account(balance = 500, int_rate=.01)
# acount2 = Account(balance= 1000, int_rate=.01)

# acount1.deposit(50)
# acount1.deposit(100)
# acount1.deposit(200)
# acount1.withdraw(200)
# acount1.yield_interest()
# acount1.display_account_info()

# acount2.deposit(50)
# acount2.deposit(100)
# acount2.withdraw(20)
# acount2.withdraw(500)
# acount2.withdraw(200)
# acount2.withdraw(100)
# acount2.yield_interest()
# acount2.display_account_info()



class User:
    def __init__(self, name, email):
        self.name= name
        self.email=email
        self.account= Account(int_rate=.01, balance=0)

    def make_deposit(self, amount):
        self.account.deposit()
    def make_withdrawal(self, amount):
        self.account.withdraw()
    def display_balance(self):
        self.account.display_account_info()
    def transfer(self, other_user, amount):
        self.balance-= amount
        other_user.balance +=amount

hanin = User(name='Hanin', email='hanin@abc.com')
jamal = User(name='Jamal', email='jamal@abc.com')
amin = User(name='Amin', email='amin@abc.com')

hanin.account.deposit(200)
hanin.account.withdraw(100)
hanin.account.display_account_info()

