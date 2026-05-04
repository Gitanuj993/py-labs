

class Hello :

    def __init__(self,radius):
        self._radius  = radius
        self.PI = 3

    @property
    def area(self):
        return self.PI * (self._radius) **2

h = Hello(5)
res = h.area()