#create account class with attributes - balance & account no
#create methods for debit ,credit, and printing the balance

class Account:
    def __init__(self, balance, accountNo):
        self.balance = balance
        self.accountNo = accountNo
        
    def debit(self,amount):
        
        if(self.balance>=amount):
            self.balance -= amount
            print(f"{amount} is debited successfully")
        else:
            print("you don't have sufficient amount in your account")
        
    def credit(self,amount):
        if(amount>0):
            self.balance += amount
            print(f"{amount} is credited successfully")
        else:
            print("Invalid amount")
    
    def balanceStatus(self):
        print(f"your current account balance:{self.balance}")
        
        
ac1 = Account(300,23344)
ac1.debit(400)
ac1.debit(200)
ac1.balanceStatus()
ac1.credit(-100)
ac1.balanceStatus()
ac1.credit(1000)
ac1.balanceStatus()