# ===============================
# 🔁 OOP Concept: Inheritance, Encapsulation, Abstraction, Polymorphism, Singleton
# ===============================
from abc import ABC, abstractmethod   # For abstract base classes (Abstraction)
from datetime import datetime         # For timestamps in transactions

# ===============================
# 📦 Singleton Pattern - Ensures one instance of AccountDatabase
# OOP Concept: Singleton, Encapsulation
# ===============================
class AccountDatabase:
    """Singleton database to store accounts"""
    _instance = None  # Class variable to hold the single instance

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(AccountDatabase, cls).__new__(cls)
            cls._instance.accounts = {}  # Dictionary to store account objects
        return cls._instance

    def add_account(self, account):
        self.accounts[account.account_number] = account

    def get_account(self, account_number):
        return self.accounts.get(account_number)

    def remove_account(self, account_number):
        if account_number in self.accounts:
            del self.accounts[account_number]
            return True
        return False

# ===============================
# 💳 Transaction Class
# OOP Concept: Encapsulation
# ===============================
class Transaction:
    """Represents a bank transaction"""
    def __init__(self, transaction_type, amount, timestamp=None):
        self.transaction_type = transaction_type  # e.g., Deposit or Withdrawal
        self.amount = amount
        self.timestamp = timestamp if timestamp else datetime.now()

    def __str__(self):
        return f"{self.transaction_type}: ${self.amount} at {self.timestamp.strftime('%Y-%m-%d %H:%M:%S')}"

# ===============================
# 🧱 Abstract Account Class (Base)
# OOP Concept: Abstraction, Encapsulation, Inheritance, Polymorphism
# ===============================
class Account(ABC):
    """Abstract class for all account types"""
    def __init__(self, account_number, owner_name, balance=0):
        self.account_number = account_number
        self.owner_name = owner_name
        self._balance = balance                  # Encapsulated with _
        self._transactions = []                  # Keeps record of transactions

    @property
    def balance(self):
        return self._balance

    @abstractmethod
    def calculate_interest(self):               # Abstract method (Abstraction)
        pass

    def deposit(self, amount):
        if amount <= 0:
            return False, "Deposit amount must be positive"
        self._balance += amount
        transaction = Transaction("Deposit", amount)
        self._transactions.append(transaction)
        return True, f"Deposited ${amount}. New balance: ${self._balance}"

    def withdraw(self, amount):
        if amount <= 0:
            return False, "Withdrawal amount must be positive"
        if amount > self._balance:
            return False, "Insufficient funds"
        self._balance -= amount
        transaction = Transaction("Withdrawal", amount)
        self._transactions.append(transaction)
        return True, f"Withdrew ${amount}. New balance: ${self._balance}"

    def get_transaction_history(self):
        return self._transactions

    def __str__(self):
        return f"{self.__class__.__name__} - Number: {self.account_number}, Owner: {self.owner_name}, Balance: ${self._balance}"

# ===============================
# 💰 Savings Account
# OOP Concept: Inheritance, Polymorphism
# ===============================
class SavingsAccount(Account):
    """Savings account with interest"""
    def __init__(self, account_number, owner_name, balance=0, interest_rate=0.01):
        super().__init__(account_number, owner_name, balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        interest = self._balance * self.interest_rate
        self.deposit(interest)
        return interest

# ===============================
# 🏦 Checking Account with Overdraft
# OOP Concept: Inheritance, Polymorphism
# ===============================
class CheckingAccount(Account):
    """Checking account with overdraft"""
    def __init__(self, account_number, owner_name, balance=0, overdraft_limit=100):
        super().__init__(account_number, owner_name, balance)
        self.overdraft_limit = overdraft_limit

    def calculate_interest(self):
        return 0  # No interest for checking accounts

    def withdraw(self, amount):
        if amount <= 0:
            return False, "Withdrawal amount must be positive"
        if amount > self._balance + self.overdraft_limit:
            return False, "Exceeds overdraft limit"
        self._balance -= amount
        transaction = Transaction("Withdrawal", amount)
        self._transactions.append(transaction)
        if self._balance < 0:
            return True, f"Withdrew ${amount}. New balance: ${self._balance} (overdraft)"
        return True, f"Withdrew ${amount}. New balance: ${self._balance}"

# ===============================
# 🏢 Bank Manager Class
# OOP Concept: Composition (uses AccountDatabase inside), Encapsulation
# ===============================
class Bank:
    """Manages creation and management of accounts"""
    def __init__(self, name):
        self.name = name
        self.database = AccountDatabase()  # Singleton instance

    def create_account(self, account_type, account_number, owner_name, initial_balance=0, **kwargs):
        if self.database.get_account(account_number):
            return False, "Account number already exists"

        if account_type.lower() == "savings":
            interest_rate = kwargs.get("interest_rate", 0.01)
            account = SavingsAccount(account_number, owner_name, initial_balance, interest_rate)
        elif account_type.lower() == "checking":
            overdraft_limit = kwargs.get("overdraft_limit", 100)
            account = CheckingAccount(account_number, owner_name, initial_balance, overdraft_limit)
        else:
            return False, "Invalid account type"

        self.database.add_account(account)
        return True, account

    def get_account(self, account_number):
        return self.database.get_account(account_number)

    def close_account(self, account_number):
        return self.database.remove_account(account_number)

# ===============================
# 🧪 Sample Test Execution
# ===============================
if __name__ == "__main__":
    bank = Bank("PyBank")

    # Create Savings Account
    success, result = bank.create_account("savings", "S12345", "Alice Smith", 1000, interest_rate=0.025)
    if success:
        print(f"Account created: {result}")

    # Create Checking Account
    success, result = bank.create_account("checking", "C67890", "Bob Johnson", 500, overdraft_limit=200)
    if success:
        print(f"Account created: {result}")

    # Retrieve accounts
    alice_account = bank.get_account("S12345")
    bob_account = bank.get_account("C67890")

    # Perform transactions
    print("\nPerforming transactions:")
    success, message = alice_account.deposit(500)
    print(message)

    success, message = alice_account.withdraw(200)
    print(message)

    success, message = bob_account.deposit(300)
    print(message)

    success, message = bob_account.withdraw(900)  # Triggers overdraft
    print(message)

    # Interest calculation
    print("\nCalculating interest:")
    interest = alice_account.calculate_interest()
    print(f"Interest earned: ${interest}")

    # Final details
    print("\nFinal account details:")
    print(alice_account)
    print(bob_account)

    # Alice's transaction history
    print("\nTransaction history for Alice:")
    for transaction in alice_account.get_transaction_history():
        print(transaction)





"""

✅ OOP Concepts Summary Used in the Code:

-----------------------------------------------------------------------------|
OOP Concept	    |   Where It's Used
----------------|------------------------------------------------------------|
Encapsulation	|   Private _balance, _transactions in Account class
----------------|------------------------------------------------------------|
Inheritance	    |   SavingsAccount and CheckingAccount inherit from Account
----------------|------------------------------------------------------------|
Abstraction	    |   Account is an abstract base class with an abstract method
----------------|------------------------------------------------------------|
Polymorphism	|   calculate_interest() behaves differently in subclasses
----------------|------------------------------------------------------------|
Singleton	    |   AccountDatabase ensures only one shared instance
----------------|------------------------------------------------------------|
Composition	    |   Bank class uses AccountDatabase to manage accounts
-----------------------------------------------------------------------------|

"""