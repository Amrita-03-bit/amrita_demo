class empolyee:

    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

    def display(self):
        print("name :",self.name)    
        print("salary :",self.salary)

account_1=empolyee("rahul",40000)
account_2=empolyee("ankit",60000)
account_1.display()
account_2.display()
