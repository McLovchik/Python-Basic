import random

errors = [
    BaseException,
    TypeError,
    TimeoutError
]

rnd = 0
with open('out_file.txt', 'w') as out_file:
    while rnd <= 777 - 1:
        nums = int(input('Введите число: '))
        rnd += nums
        if 13 == random.randint(1, 13):
            print('Вас постигла неудача!')
            raise Exception(random.choice(errors))
        print(nums, file=out_file)
    print('Вы успешно выполнили условие для выхода из порочного цикла!')
