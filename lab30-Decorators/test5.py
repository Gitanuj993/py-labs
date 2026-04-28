def my_decorator(f) :
    def wrapper() :
        print("Before decoration")
        f()
        print("After decorations")
    return wrapper

def f() :
    print(" This is the decorated function ")


f()