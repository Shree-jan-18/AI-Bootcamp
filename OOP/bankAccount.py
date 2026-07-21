class BankAccount:
    def __init__(self, balance):
        self.__balance = balance      # Private variable

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient Balance")

    def show_balance(self):
        print("Current Balance =", self.__balance)


# Creating object
account = BankAccount(1000)

#Encapsulation: Accessing private variable through public methods
account.deposit(500)
account.withdraw(300)
account.show_balance()