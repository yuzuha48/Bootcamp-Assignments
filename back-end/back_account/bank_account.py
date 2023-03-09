class BankAccount:
    accounts = []
    def __init__(self, interest, balance = 0):
        self.balance = balance
        self.interest = interest/100 
        BankAccount.accounts.append(self) 
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5 
        return self
    def display_account_info(self):
        print(f"Balance: {self.balance}")
        return self
    def yield_interest(self):
        self.balance += self.balance * self.interest
        return self
    @classmethod
    def print_all_accounts(cls):
        for i in cls.accounts:
            i.display_account_info()

yuzuha_account = BankAccount(1, 100)
jackson_account = BankAccount(2, 1000)

yuzuha_account.deposit(100).deposit(100).deposit(100).withdraw(100).yield_interest()

jackson_account.deposit(100).deposit(100).withdraw(200).withdraw(300).withdraw(100).withdraw(100).yield_interest()

BankAccount.print_all_accounts()
