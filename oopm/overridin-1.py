class super :
    def multiply(self,a,b):
        self.a = a + 1 # self.a = 1 then self.a = self.a + 1
        self.b = b
        print(self.a)
        # default constructor will run first.



class sub(super) :
    pass
    # method is not overridden
    # empty class or empty functions are not entertained.


if __name__ == '__main__':
    sub1 = sub() # it will call constructor of 
    sub1.multiply(1,2)