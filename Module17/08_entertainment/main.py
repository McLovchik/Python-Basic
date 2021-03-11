import random

sticks = int(input('Кол-во палок: '))
throws = int(input('Кол-во бросков: '))

sticks_list = ['I' for _ in range(sticks)]

for i_throw in range(throws):
    shot_down_left = random.randint(1, sticks)
    shot_down_right = random.randint(1, sticks)
    if shot_down_left > shot_down_right:
        shot_down_left, shot_down_right = shot_down_right, shot_down_left
    print(f'Бросок {i_throw + 1}. Сбиты палки с номера {shot_down_left} по номер {shot_down_right} ')
    number_shot_down = shot_down_right - shot_down_left + 1
    sticks_list[shot_down_left - 1:shot_down_right] = ['.' for _ in range(number_shot_down)]

print(sticks_list)

# TODO, пожалуйста, выведите результат исходя из примера
#  Результат: I.....I...

# создать новую переменную и добавлять с помощью "+"?
