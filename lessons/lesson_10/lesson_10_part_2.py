from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass

class Square(Shape):
    def __init__(self, side):
        self.__side = side

    def area(self):
        return self.__side ** 2

    def perimeter(self):
        return self.__side * 4

    def __str__(self):
        return f'Square with side {self.__side} has an area of {self.area()} and a perimeter of {self.perimeter()}'

class Rectangle(Shape):
    def __init__(self, side1, side2):
        self.__side1 = side1
        self.__side2 = side2

    def area(self):
        return self.__side1 * self.__side2

    def perimeter(self):
        return (self.__side1 + self.__side2) * 2

    def __str__(self):
        return f'Rectangle with side {self.__side1} and side {self.__side2} has a area of {self.area()} and a perimeter of {self.perimeter()}'


class Circle(Shape):
    def __init__(self, radius):
        self.__radius = radius

    def area(self):
        return (self.__radius **2) * 3.14

    def perimeter(self):
        return 2 * 3.14 * self.__radius

    def __str__(self):
        return f'Circle with radius {self.__radius} has an area of {round(self.area(), 2)} and a perimeter of {round(self.perimeter(), 2)}'

square_1 = Square(6)

rectangle_1 = Rectangle(5, 8)

circle_1 = Circle(10)

print(square_1)
print(rectangle_1)
print(circle_1)


