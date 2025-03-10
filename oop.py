class Account:

    def __init__(self, account_number, account_balance, account_holder):
        self.account_number = account_number
        self.account_balance = float(account_balance)
        self.account_holder = account_holder
    def __str__(self):
        return f"Your account number is: {self.account_number}\nAnd your account name is {self.account_holder} \nAnd your account balance is {self.account_balance}"
    
    def deposite(self, amount):
        self.account_balance += amount
        return f"your new account balance is: {self.account_balance}"
    def withdraw(self, amount):
        if amount > self.account_balance:
            return f"sorry insuficent fund: your current balance is {self.account_balance}"
        self.account_balance -= amount
        return f"Your withdrawal was successfull, Your Account Balance is Now:{round(self.account_balance, 2)} "
    def check_balance(self):
        user_input=input("kindly type in your account number: ")
        if user_input == self.account_number:
            return f"Your current account balance is:{self.account_balance}"
        else:
            return f"incorrect account number"

my_account = Account(account_number="2081551853", account_balance=20000.345, account_holder="francis chizey")
account_1 = Account(account_number=" 2081551854", account_balance=53000.231, account_holder="fikayo moni")
account_2 = Account(account_number="2081551855", account_balance=43000.400, account_holder="chidma ada")
# print(my_account.deposite(10000))
# print(my_account.withdraw(5000))
# print(my_account.check_balance())
# print(account_1.deposite(30000))
# print(account_1.withdraw(80000))
print(account_2.deposite(28000))