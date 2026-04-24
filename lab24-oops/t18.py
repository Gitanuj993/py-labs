
# class 1
class Class_base :
    def method(self):
        print(" i am a public method ")
    def _method(self):
        print(" i am a protected method")
    def __method(self):
        print(" i am private method")


# sub class
class Sub_class :
    def method(self):
        s = Class_base()
        s.method() # public method of base class run
        s._method() # protected method of base class run
        # protected method of above class
        # s.__method() # AttributeError: 'Class_base' object has no attribute '_Sub_class__method'


if __name__ == "__main__" :
    # creating object of subClass
    s = Sub_class()
    s.method()

