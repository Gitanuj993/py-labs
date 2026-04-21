class Car:
    wheels = 4  # class variable

    def __init__(self, brand):
        self.brand = brand  # instance variable

car1 = Car("Toyota")
car2 = Car("Honda")

print(car1.wheels)  # 4
print(car2.wheels)  # 4
print(Car.wheels) # using class name via dot operator