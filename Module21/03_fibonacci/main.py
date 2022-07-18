def fibonacci(pos):
    if pos in (1, 2):
        return 1
    return fibonacci(pos - 1) + fibonacci(pos - 2)


position = int(input('Введите позицию числа в ряде Фибоначчи: '))
print(fibonacci(position))
