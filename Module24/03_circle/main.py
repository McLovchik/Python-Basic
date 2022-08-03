import math


class Circle:
    def __init__(self, x=0, y=0, r=1):
        self.x = x
        self.y = y
        self.r = r

    def area(self):
        area_of_a_circle = math.pi * self.r ** 2
        return area_of_a_circle

    def perimeter(self):
        circle_perimeter = 2 * math.pi * self.r
        return circle_perimeter

    def increase(self, k):
        self.r = self.r * k
        new_area = self.area()
        return new_area

    def intersection(self, other):
        dist_sq = (self.x - other.x) ** 2 + (self.y - other.y) ** 2
        rad_sum_sq = (self.r + other.r) ** 2
        if dist_sq == rad_sum_sq:
            print('Круги касаются')
        elif dist_sq > rad_sum_sq:
            print('Круги не пересекаются')
        else:
            print('Круги перескаются')
