def my_decorator(f) :
    def wrapper() :
        print("Before decorating ")
        hello_guys()
        print("After decoration ! ")
        return "Nothing_return"
    return wrapper()

@my_decorator
def hello_guys() :
    print(" Hello gentlemen, welcome to the party.")

my_decorator(hello_guys())


