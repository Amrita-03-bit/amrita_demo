class bankaccount:

    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
    
    def withdraw(self,amount):
            try:
             if amount>self.balance:
                print("insufficent balance")

             else:
                self.balance-=amount
                print(self.balance)   
            except ValueError:
             print("abc")

b1=bankaccount("shreya",40000)
b2=bankaccount("ishika",654322)

b1.withdraw(8765668)
b2.withdraw(5434)
