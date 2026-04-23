# method overriding

class Super :

    def multiply(self):
        print("multiply of class super")


class Sub(Super) :
    def multiply(self):
        print("multiply of class sub")




if __name__ == "__main__":
    # object of subclass
    sub1 = Sub()
    # calling function which is available in both <superclass> and <subclass>
    sub1.multiply()
    # which method of class
    # functionality of base class is used in subclass with its own implementation.