def withdraw(accno,amount) :
    bal = 5000
    if bal > amount :
        bal-=amount
        return bal
    else :
        print(" Balance is too low !, unable to withdraw Money")
        return 1

# core business logic written in core python , core java contacting with databases and other modules

print(withdraw(1,234000))