# default constructor
class Customer :

    def __init__(self,a,b,c):
        print(" Welcome to the class")


# a,b,c = 0
a,b,c = 0,0,0
obj1 = Customer(a,b,c)

# Error case try this
# calling default constructor , default constructor is not declared yet
# obj2 = Customer()
# TypeError: Customer.__init__() missing 3 required positional arguments: 'a', 'b', and 'c'