class bankaccount:

    def __init__(self,name,balance):
        self.name=name
        self.balance=balance

    def deposit(self,amount):
        self.balance+=amount

    def withdraw(self,amount):
        if amount<=self.balance:
            self.balance-=amount

account=bankaccount("rahula",500000)
account.deposit(356772)
account.withdraw(56776)
print(account.balance)
