# Multiple inheritance -  ambiguity
# method resolution order

class A :
    def __init__(self):
        self.a = 12



class B(A) :
    def __init__(self):
        self.a = 12


class C(A) :
    def __init__(self):
        self.a = 12


if __name__ == "__main__" :

