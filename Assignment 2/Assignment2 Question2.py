class BankAccount:
    def __init__(self, account_holder, opening_balance=0):
        self.account_holder = account_holder
        self.__balance = opening_balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"${amount:.2f} deposited successfully.")
        else:
            print("The deposit amount must be greater than zero.")

    def withdraw(self, amount):
        if amount <= 0:
            print("The withdrawal amount must be greater than zero.")
        elif amount > self.__balance:
            print("Withdrawal failed: insufficient funds.")
        else:
            self.__balance -= amount
            print(f"${amount:.2f} withdrawn successfully.")

    def display_balance(self):
        print(f"Current balance: ${self.__balance:.2f}")

    def get_balance(self):
        return self.__balance


# Create a bank account
account = BankAccount("Romeo Chinakidzwa", 1000)

print("Account holder:", account.account_holder)
account.display_balance()

# Deposit money
account.deposit(500)

# Withdraw money
account.withdraw(300)

# Display the updated balance
account.display_balance()

# Trying to access the private attribute directly
try:
    print(account.__balance)
except AttributeError:
    print("The balance cannot be accessed directly because it is private.")