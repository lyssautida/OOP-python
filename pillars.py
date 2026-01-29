# Inheritance eg
print("\nInheritance eg")
class Animal:
    def __init__(self, name) -> None:
        self.name = name
    
    def walk(self):
        print(f"The animal {self.name} has walked")
        return
    
    def sound(self):
        pass


class Doggie(Animal):
    def sound(self):
        return "wan, wan"
    
    
class Kitten(Animal):
    def sound(self):
        return "nyan"
    

dog = Doggie(name="Scot")
cat = Kitten(name="Pixie")

print("\nPolimorfism eg")
animals = [dog, cat]

for animal in animals:
    print(f"{animal.name} makes: {animal.sound()}")

print("\nencapsulation eg")
class BankAccount:
    def __init__(self, balance) -> None:
        self.__balance = balance #private attribute

    def deposit(self, value):
        if value > 0:
            self.__balance += value
    
    def withdraw (self, value):
        if value > 0 and value <= self.__balance:
            self.__balance -= value

    def check_balance (self):
        return self.__balance 
    
account = BankAccount(balance=1000)
print(f"Bank Account Balance: {account.check_balance()}")
account.deposit(value=500)
print(f"Bank Account Balance: {account.check_balance()}")
account.deposit(value=500)
print(f"Bank Account Balance: {account.check_balance()}")
account.withdraw(value=2000)
print(f"Bank Account Balance: {account.check_balance()}")





