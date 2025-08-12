class Account:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance
    
    def get_balance(self):
        print(f"Balance: {self.__balance}")
        
    def deposite(self, deposite):
        self.__balance += deposite
        print(f"Balance: {self.__balance}")
        
    def withdraw(self, withdraw):
        if self.__balance > withdraw:
            self.__balance -= withdraw
            print(f"Balance: {self.__balance}")
        else:
            print("Insufficient balance")

ac1 = Account("tom", 10000)
ac1.get_balance()
ac1.withdraw(100)
ac1.deposite(1000)
ac1.withdraw(50000)

ac2 = Account("Arun", 30000)
ac1.get_balance()
ac1.withdraw(500)
ac1.deposite(25000)
ac1.withdraw(300)
