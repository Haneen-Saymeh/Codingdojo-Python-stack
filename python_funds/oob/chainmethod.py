class User:
    def __init__(self, name, email):
        self.name= name
        self.email=email
        self.balance=0
    def make_deposit(self, amount):
        self.balance += amount
        return self
    
    def make_withdrawal(self, amount):
        self.balance -=amount
        return self
    
    def display_balance(self):
        print('User name:', self.name, "\nUser's balance:", self.balance)
        return self
    
    def transfer(self, other_user, amount):
        self.balance-= amount
        other_user.balance +=amount

hanin = User(name='Hanin', email='hanin@abc.com')
jamal = User(name='Jamal', email='jamal@abc.com')
amin = User(name='Amin', email='amin@abc.com')



hanin.make_deposit(200).make_deposit(100).make_deposit(100).make_deposit(300).display_balance()

jamal.make_deposit(400).make_deposit(200).make_withdrawal(100).display_balance()

amin.make_deposit(100).make_withdrawal(100).make_withdrawal(50).make_withdrawal(50).display_balance()



hanin.transfer(amin, 200)
hanin.display_balance()
amin.display_balance()