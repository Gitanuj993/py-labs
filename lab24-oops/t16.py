# instance variables and class variables

class Test :
    # by default scope is public
    a = 0
    b = 0
    def __init__(self,a,b):
        self.a = a
        self.b = b
        print(" instance variables initialized !")
    def show_instance_var(self):
        print(f"object var_a : {self.a , self.b } ")
    print("="*22)
    @classmethod
    def showClass(cls) :
        print(f"object var_a : {cls.a , cls.b , } ")




if __name__ == "__main__" :
    s1 = Test(11,22)
    s1.show_instance_var()
    s1.showClass()
