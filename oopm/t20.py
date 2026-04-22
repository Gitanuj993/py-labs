# Define a class
class Person:
    # Constructor (initializer)
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Method
    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

# Create an object (instance)
p1 = Person("Alice", 25)
# what is p1 ? is it hold is name or age ?
print(p1) # it prints address of the object .

del p1 # it will delete object reference and the object itself

