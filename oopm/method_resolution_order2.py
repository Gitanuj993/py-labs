
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
    pass


if __name__ == "__main__":
    # object of class D
    d1 = D()
    d1.show()
    # what if we remove show function of class D and then try to call show
    # it is defined by Method resolution order , we can know the <MRO> order of any class by
    print("Method Resolution Order of class D is :",D.mro(),sep=" ")
    print(f"MRO of class A is : {A.mro()}")
    print(f"MRO of class B is : {B.mro()}")
    print(f"MRO of class C is : {C.mro()}")
    print(f"MRO of class D is : {D.mro()}")
    # __main__ is a package
