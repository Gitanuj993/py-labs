# is constructor of subclass automatically call constructor of superclass

# inheritance Single inheritance

class Super : # 'Super' is super class of class 'Sub'
    def __init__(self):
        print(" i am the super class")

class Sub(Super) : # 'Sub' is a subclass of class 'Super'
    def __init__(self):
        print("Welcome to the subclass")

if __name__ == "__main__" :
    # object of subclass
    sub1 = Sub()
    # default constructor of the superclass do not call automatically by the __init__ of subclass.
