# class
class Accounts :
    # parameterized constructor
     def __init__(self,ac_no,name,ac_type ="Saving",bal = 0,phone = None):
         # initializing values into instance variables
         self.ac_no = ac_no
         self.name = name
         self.ac_type = ac_type
         self.bal = bal
         self.phone_no = phone
        # what if we use class name to access and change instance variables

    # deposit function
     def deposit(self,amount) :
        prev_bal = self.bal
        self.bal += amount
        print(f" your account has been credited with {amount} ")
        print(f" Now your balance is : {self.bal}")
        return self.bal

    # withdraw money
     def withdraw(self,amount) :
        if ( self.bal > 0 and self.bal <= amount) :
            self.bal -= amount
            print(f" Your account has been debited with {amount}")
            print(f" Now remaining balance is : {self.bal}")

        else :
            print(f" You do not have sufficient amount for withdrawal")

    # show function to display customer details
     def display_bal(self) : # display_info  is a behavior of the object
        print(f" account_no : {self.ac_no}")
        print(f" Name : {self.name}")
        print(f" is an '{self.ac_type}' account having bal : {self.bal}")

# main function
if __name__ == "__main__" :

    # object
    c1 = Accounts(1,"AT","Saving",200000,626)
    c1.display_bal()
    # While True
    while True :
        print(" Choose what operations you want to perform !\n")
        print(" 1. for new account !")
        print(" 2. for balance withdrawal ")
        print(" 3. for money deposit")








