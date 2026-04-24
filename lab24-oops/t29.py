# inheritance Single inheritance

class Super : # 'Super' is super class of class 'Sub'
    def __init__(self):
        print(" i am the super class")
        self.a = 10

    def _show(self):
        print(f" a : {self.a}")


class Sub(Super) : # 'Sub' is a subclass of class 'Super'
    def __init__(self):
        print("Welcome to the subclass")
        # calling constructor of base class from the subclass.
        # super().__init__()

    def show(self):
        # let's print value of a which is from the superclass.
        print(f" Value of a is : {self.a}")
        #AttributeError: 'Sub' object has no attribute 'a'
        # we have to call constructor inorder to access instance variables of super class.



if __name__ == "__main__" :
    sup1 = Super() # constructor of super is called a is initialized to 10
    s1 = Sub()
    s1._show() # Error
