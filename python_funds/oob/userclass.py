class User:
    def __init__(self, name, email):
        self.name= name
        self.email=email
        self.balance=0
    def make_deposit(self, amount):
        self.balance += amount
    def make_withdrawal(self, amount):
        self.balance -=amount
    def display_balance(self):
        print('User name:', self.name, "\nUser's balance:", self.balance)
    def transfer(self, other_user, amount):
        self.balance-= amount
        other_user.balance +=amount

hanin = User(name='Hanin', email='hanin@abc.com')
jamal = User(name='Jamal', email='jamal@abc.com')
amin = User(name='Amin', email='amin@abc.com')

hanin.make_deposit(200)
hanin.make_deposit(100)
hanin.make_deposit(300)
hanin.display_balance()

jamal.make_deposit(400)
jamal.make_deposit(200)
jamal.make_withdrawal(100)
jamal.make_withdrawal(50)
jamal.display_balance()

amin.make_deposit(100)
amin.make_withdrawal(100)
amin.make_withdrawal(50)
amin.make_withdrawal(50)
amin.display_balance()

hanin.transfer(amin, 200)

hanin.display_balance()
amin.display_balance()