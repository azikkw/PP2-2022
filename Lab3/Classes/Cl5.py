#Bank account

class Account:
    
    def __init__(self, owner, balance, deposit, withdraw):
        self.owner = owner
        self.balance = balance
        self.deposit = deposit
        self.withdraw = withdraw
        
    def about(self):
        print([self.owner, self.balance, self.deposit, self.withdraw])
        
    def f(self):
        if self.balance >= self.withdraw:
            print("The amount does not exceed the balance amount. Please keep your money.", "Balance:", self.balance, "->", "Withdraw:", self.withdraw)
        else:
            print("The amount exceeds the balance amount.", "Balance:", self.balance, "->", "Withdraw:", self.withdraw)
            
            
            
Azat = Account("Amen Azat", 200000, 1000000, 80000)
Arman = Account("Burkutbaev Arman", 300000, 800000, 500000)
Dilnar = Account("Beisenbaev Dilnar", 150000, 2000000, 50000)


Azat.about()
Azat.f()

Arman.about()
Arman.f()

Dilnar.about()
Dilnar.f()