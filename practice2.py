class BankAccount(object):
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def show_balance(self):
        print("Balance :",self.balance)

    def Deposit(self, newbalance):
        self.balance += newbalance
        print("Balance:", self.balance)

    def WithDraw(self, amtToWithDraw):
        if(amtToWithDraw > self.balance):
            print("You poor dont have enough Money!")
            return
        self.balance -= amtToWithDraw
        print("Balance:",self.balance)


Shubham = BankAccount("Shubham", 99)
Shubham.show_balance()
Shubham.Deposit(1)
Shubham.WithDraw(101)