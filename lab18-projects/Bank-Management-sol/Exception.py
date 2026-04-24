class UnsufficientBalanceError(Exception):
    def __init__(self,balance):
        self.bal= balance
        super().__init__(f"UnsufficientBalance, balance : {balance} !")

class NegativeBalanceError(Exception):
    def __init__(self):
        super().__init__(" Amount can not be negative")
