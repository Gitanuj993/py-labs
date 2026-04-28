# decorator adding additional things to the existing function.
def my_decorator(f) : # taking function as a parameter
    def wrapper() : # a function inside function , additional functionality is added here
        print("Before decoration")
        f()
        print("After decorations")
        #
    return wrapper
@my_decorator
def f() :
    print(" This is the decorated function ")

# calling function
f()
"""
Flow of execution is
14 , 10,9,2,3,4,5,10,11,6,7,8,

"""