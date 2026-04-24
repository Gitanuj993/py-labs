# class declaration
class Order:
    app = "IPT" # can be access through object reference , self, class reference
    sub_discount = "40%"

    def __init__(self, ord_id, level):
        self.ord_id = ord_id
        self.level = level

    def show(cls):
        print(Order.app, Order.sub_discount, sep=" ")
        Order.sub_discount = "30%"
        print(Order.app, Order.sub_discount, sep=" ")
        # let's try to change class data using self method or instance method
        # self.sub_discount = "60%" # self is not defined
    def show(self):
        pass
    # let's try to change class data using self method or instance method
        self.sub_discount = "60%" # self is not defined
        print(Order.app, Order.sub_discount, sep=" ")
        # changes not appear.


o1 = Order(1,1)
o1.show()