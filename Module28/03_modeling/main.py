from abc import ABC, abstractmethod
import math


class Figure(ABC):
    """
    Абстрактный базовый класс фигуры

    Args:
        side (int): размер стороны фигуры
    """
    def __init__(self, side: int):
        self.side = side

    @abstractmethod
    def get_perimeter(self):
        pass


class Square(Figure):
    """ Квадрат """
    def __init__(self, side: int):
        super().__init__(side)

    def get_perimeter(self):
        return self.side * 4

    def get_square(self):
        return self.side ** 2


class Triangle(Figure):
    """
    Треугольник

    Args:
        height (int): высота
    """
    def __init__(self, side: int, height: int):
        super().__init__(side)
        self.height = height

    def get_perimeter(self):
        return self.side + 2 * math.sqrt((self.side / 2) ** 2 + self.height ** 2)

    def get_square(self):
        return 0.5 * self.side * self.height


class Cube(Square):
    """ Куб """
    def __init__(self, side: int):
        super().__init__(side)

    def get_square(self):
        sq_square = super().get_square()
        return 6 * sq_square


class Pyramid(Triangle):
    """ Пирамида """
    def __init__(self, side: int, height: int):
        super().__init__(side, height)

    def get_square(self):
        sq_triangles = super().get_square()
        return 4 * sq_triangles + self.side ** 2
