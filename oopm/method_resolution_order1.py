#

class A :

    def show(self):
        print(" i am show function of class A")

class B(A) :

    def show(self):
        print(" i am show function of class B")

class C(A) :
    def show(self):
        print(" i am show function of class C")

class D(B,C) :
    def show(self):
        print(" i am show function of D")


if __name__ == "__main__":
    # object of class D
    d1 = D()
    d1.show()
    # what if we remove show function of class D and then try to call show
