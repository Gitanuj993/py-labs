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
        # let's try to access value of 'a' which is class variable of class A
        print(f" Class A a : {self.a}")
        # run kiya



if __name__ == "__main__" :
    # object of class C
    c1 = C()
    c1.showC()
    print(f" a is : {c1.a}")
    print(f" b is : {c1.b}")
