# inheritance Single inheritance

class Super : # 'Super' is super class of class 'Sub'
    def __init__(self):
        self.a = 10

    def _show(self):
        print(f" a : {self.a}")


class Sub(Super) : # 'Sub' is a subclass of class 'Super'
    def __init__(self):
        print("Welcome to the subclass")

    def show(self):
        # let's print value of a which is from the superclass.
        print(f" Value of a is : {self.a}")
        #AttributeError: 'Sub' object has no attribute 'a'
        # we have to call constructor inorder to access instance variables of super class.



if __name__ == "__main__" :
    s1 = Sub()
    s1._show()
    # we are trying to achieve inheritance but we unable to print value of instance varible 'a'
    # as we didn't create object of superclass thus instance variable is not known.
