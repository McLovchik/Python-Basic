# Пользователь вводит число N.
# Напишите программу, которая генерирует последовательность из квадратов чисел
# от 1 до N (1 ** 2, 2 ** 2, 3 ** 2 и так далее).
# Реализацию напишите тремя способами: класс-итератор, функция-генератор и генераторное выражение.

# класс-итератор
class Squares:
    def __init__(self, n):
        self.n = n
        self.i = 0
        self.squares_list = []

    def __iter__(self):
        self.i = 0
        return self

    def __next__(self):
        while self.i < self.n:
            self.i += 1
            return self.i ** 2
        raise StopIteration


squares_list = Squares(6)
for j in squares_list:
    print(j)

#
print()
#


# функция-генератор


def squares(n):
    i = 0
    while i < n:
        i += 1
        yield i ** 2


squares_list = squares(6)
for j in squares_list:
    print(j)

#
print()
#

# генераторное выражение
squares_list = [i ** 2 for i in range(1, 7)]
for j in squares_list:
    print(j)
