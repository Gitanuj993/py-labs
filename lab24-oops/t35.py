# Multiple Inheritance

class A :
    a = 1

    def showA(self):
        print(" I am class A ", A.a)


class B:
    b = 1

    def showB(self):
        print(" I am class B ", B.b)



class C(A,B):
    c = 11

    def showC(self):
        print(f" c is : {self.c}")



if __name__ == "__main__" :
    # object of class C
    c1 = C()
    c1.showA()
    c1.showB()

