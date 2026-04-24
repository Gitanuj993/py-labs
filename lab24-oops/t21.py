# Define a class
class Person:
    # Constructor (initializer)
    def __init__(self, name = None, age = None , job = None):
        self.name = name
        self.age = age

    # Method
    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")


# what if we want to delete a attribute of an object

p1 = Person()
p2 = Person("AT",21,"SDE")
# person 1
p1.greet()
# person 2
p2.greet()

# we want to delete age attribute
del p1.age
p1.greet()
# AttributeError: 'Person' object has no attribute 'age'
