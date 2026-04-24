# default parameters and keyword parameters

class Student:
    def __init__(self, name, age ,std = None):
        self.name = name      # instance variable d
        self.age = age        # instance variable
        self.std = std

s1 = Student("Rahul", 20)
s2 = Student("Anita", 22,12)

print(s1.name)  # Rahul
print(s2.name)  # Anita
