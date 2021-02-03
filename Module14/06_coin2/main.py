from math import sqrt

print('Введите координаты монетки: ')
x = float(input('Коорд-та x: '))
y = float(input('Коорд-та y: '))
r = float(input('Введите радиус: '))

distance_fron_zero = sqrt(x ** 2 + y ** 2)

def find(distance,radius):
  if distance_fron_zero <= r:
    print('Монетка где-то рядом')
  else:
    print('Монетки в области нет')  

find(distance_fron_zero, r)