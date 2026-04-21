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



print('......................................................................')

#modify password using private class

class Modify:
    def __init__(self,id, old_pas, new_pas):
        self.id = id
        self.old_pas = old_pas
        self.__new_pas = new_pas        # private attribute bcz use double undersore in start

    def showpassword(self):
        return(
            f"The {self.id}'s account old password = {self.old_pas}."
            f" The {self.id}'s account new password = {self.__new_pas}."
            )


Acct = Modify('Mera', 5678, 1234)
Acct1 = Modify('daneen', 5498, 'dt45')
Acct2 = Modify('huma', 'xyzt', 8765)

# call the public attributes
print(Acct.id, Acct.old_pas)
print(Acct1.id, Acct1.old_pas)
print(Acct2.id )

# did not call the private attribute its give error
# print(Acct2.id, Acct2.__new_pas )        its give error


#call the method to diplay private attribute
print(Acct.showpassword())
print(Acct1.showpassword())
print(Acct2.showpassword())