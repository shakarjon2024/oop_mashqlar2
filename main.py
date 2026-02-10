
# 1 - misol
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __repr__(self):
        return f"Product(name={self.name!r}, price={self.price})"

print(Product("Mouse", 150))




# 2 - misol
class Task:
    def __init__(self, title, done=False):
        self.title = title
        self.done = done

    def __repr__(self):
        return f"Task(title={self.title!r}, done={self.done})"

t = Task("OOP organish")
print('Yangi task:', t)



# 3 - misol
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        if amount <= 0:
            return False
        self.__balance += amount
        return True

    def withdraw(self, amount):
        if amount <= 0:
            return False
        if amount > self.__balance:
            return False
        self.__balance -= amount
        return True

    def get_balance(self):
        return self.__balance

acc = BankAccount("Alim", 100)
print(acc.withdraw(500))
print(acc.withdraw(30))
print(acc.get_balance())




# 4 - misol
class Result:
    def __init__(self, ok, message):
        self.ok = ok
        self.message = message

class Wallet:
    def __init__(self, balance):
        self._balance = balance

    def pay(self, amount):
        if amount <= 0:
            return Result(False, 'amount 0 dan katta bolsin')
        if amount > self._balance:
            return Result(False, 'pul yetarli emas')
        self._balance -= amount
        return Result(True, "tolov muvaffaqiyatli")

w = Wallet(50)
res = w.pay(100)
print(res.ok, res.message)



# 5 - misol
class Logger:
    def log(self, msg):
        print("LOG:", msg)

class Service:
    def __init__(self, logger):
        self.logger = logger  

    def run(self):
        self.logger.log("run")

Service(Logger()).run()
