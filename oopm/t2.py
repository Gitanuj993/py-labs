# class customer example

class Customer :
    # variable may or may not declare here

    def __init__(self,name,id,):
        self.name = name
        self.id = id

    def show(self):
        print(f" Customer id : {self.id} , Name is : {self.name}")



c1 = Customer("AT",1)
c1.show() # no self is passed

c2 = Customer("AT",1)
c2.show()

c3 = Customer("AT",1)
c3.show()

