import math


class Automobile:
    def __init__(self, x, y, alpha):
        self.x = x
        self.y = y
        self.alpha = alpha

    def __str__(self):
        return f'Координата x - ({self.x})\nКоордината y - ({self.y})\nУгол - ({self.alpha})'

    def move(self, distance):
        self.x = self.x + distance * math.cos(self.alpha)
        self.y = self.y + distance * math.sin(self.alpha)

    def turn(self, fun_alpha):
        fun_alpha %= 360
        self.alpha = fun_alpha


class Bus(Automobile):
    pay_coefficient = 0.01
    max_passengers = 60

    def __init__(self, x, y, alpha):
        super().__init__(x, y, alpha)
        self.passengers = 0
        self.money = 0

    def move(self, distance):
        self.money += self.pay_coefficient * self.passengers * distance
        super().move(distance)

    def enter(self, fun_passengers):
        if fun_passengers + self.passengers > self.max_passengers:
            print(f'Достигнута максимальная вместимость автобуса - {self.max_passengers} человек')
            print(f'В автобус не попало {self.passengers + fun_passengers - self.max_passengers} человек')
            self.passengers = self.max_passengers
        else:
            print('Все вместились')
            self.passengers += fun_passengers

    def exit(self, fun_passengers):
        print(f'Выходят {fun_passengers} человек')
        self.passengers -= fun_passengers

    def __str__(self):
        info = super().__str__()
        info = '\n'.join(
            (
                info,
                f'Количество пассажиров - {self.passengers}',
                f'Денег - {round(self.money, 2)}'
            )
        )
        return info
