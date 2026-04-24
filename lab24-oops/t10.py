# constructor overloading in python
# python is an interpreted programming language.

class Class1 :
    def __init__(self):
        print(" constructor1 ! ")
    def __init__(self,a):
        print(f"constructor 2 : {a}")
    def __init__(self,a,b):
        print(f"constructor 3 : {a,b}")


if __name__ == "__main__" :
    s1 = Class1() # cconstructor1
    s2 = Class1(1) # constructor 2
    s2 = Class1(1,2) # constructor 3

## python do not support constructor overloading and function overloading
## we can declare many constructors but constructor defined at last will be considered as constructor







