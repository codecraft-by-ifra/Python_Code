class Bank:
    def __init__(self, acc, bal):
        self.account = acc
        self.balance = bal

    def debit (self, amount):
        self.balance -= amount
        print(f'The {amount} is deducted from your account')
        print(f'The total balnce is : {self.get_balance()} ')

    def credit (self, amount):
        self.balance += amount
        print(f'The {amount} is added to your account')
        print(f'The total balance is : {self.get_balance()} ')

    def get_balance(self):
        return self.balance
    

acc1 = Bank(3421 , 5000)
acc2 = Bank(7865, 8000)
acc3 = Bank(9087, 2000)

acc1.credit(1000)
acc2.credit(4000)
acc3.credit(500)
acc1.debit(500)
acc2.debit(1500)
acc3.debit(3500)
acc3.credit(1000)
