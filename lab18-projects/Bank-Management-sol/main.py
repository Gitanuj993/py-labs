# import Exception
class UnsufficientBalanceError(Exception):
    def __init__(self,balance):
        self.bal= balance
        super().__init__(f"UnsufficientBalance, balance : {balance} !")

class NegativeBalanceError(Exception):
    def __init__(self):
        super().__init__(" Amount can not be negative")

# class Bank
from abc import ABC , abstractmethod

class Bank(ABC) :
    pass
    #common

class Operations(Bank) :
    def __init__(self,bal = 0.0):
        self.bal = bal

    # withdrawal
    def withdraw(self,bal,amount):
        if amount > self.bal :
            raise UnsufficientBalanceError(self.bal)
        elif amount <= 0 :
            raise NegativeBalanceError
        else :
            self.bal -= amount
            print(f" Amount : {amount} debited successfully ! ")
            print(f" balance left is : {bal}")

    def get_bal(self):
        return self.bal
    def deposit(self,amount):
        self.bal += amount
        print(" successfully deposited ")








# Input validation
if __name__ == "__main__" :
    c = Operations(20000)
    bal = c.get_bal()
    try :
        amount = int(input("Enter amount to withdraw : "))
    except ValueError :
        print(" Please Enter numbers only !")
    else : # else can't be with try block , else came in last
        c.withdraw(bal,amount)
    finally:
        print(" Resources released successfully !,")

