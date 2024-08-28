from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod # abstract method declaration
    def area(self):
        pass

    # we can declare any function with abstractmethod
    def info(self):
        return  f"This is a {type(self).__name__}"

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return f'Square are with side: {self.side} is {self.side **2}'

class Triangle(Shape):
    def __init__(self, base, hight):
        self.base = base
        self.hight = hight

    def area(self):
        return f'Triangle area with Base: {self.base} and Height: {self.hight} is {(self.base * self.hight)/2}'

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return f'Circle area with radius {self.radius} is {3.14 * self.radius **2}'



square = Square(7)
print(square.area())
print(square.info())

triangle = Triangle(7,5)
print(triangle.area())
print(triangle.info())

circle = Circle(7)
print(circle.area())
print(circle.info())
