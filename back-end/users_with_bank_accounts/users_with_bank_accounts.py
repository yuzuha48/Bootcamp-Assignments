class BankAccount:
    accounts = 0
    def __init__(self, interest, balance = 0):
        self.balance = balance
        self.interest = interest/100 
        BankAccount.accounts += 1 
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
    def all_instances(cls):
        print(f"There are {cls.accounts} accounts.")

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.checking = BankAccount(interest = 2, balance = 0)
        self.savings = BankAccount(interest = 2, balance = 1000)
    def make_deposit(self, amount, account):
        if account == "checking":
            self.checking.deposit(amount)
        if account == "savings":
            self.savings.deposit(amount)
        return self
    def make_withdrawal(self, amount, account):
        if account == "checking":
            self.checking.withdraw(amount)
        if account == "savings":
            self.savings.withdraw(amount)
        return self
    def display_user_balance(self):
        print(f"Checking: {self.checking.balance}")
        print(f"Savings: {self.savings.balance}")
        return self
    def transfer_money(self, amount, other_user):
        self.checking.balance -= amount
        other_user.checking.balance += amount


yuzuha = User("Yuzuha", "yuzuha48@gmail.com")
yuzuha.make_deposit(300, "checking").make_deposit(2000, "savings").display_user_balance()

jackson = User("Jackson", "jmuehl@umn.edu")
jackson.display_user_balance()

yuzuha.transfer_money(100, jackson)

yuzuha.display_user_balance()
jackson.display_user_balance()