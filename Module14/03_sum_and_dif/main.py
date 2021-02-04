number = int(input('Введите число: '))

# TODO: До и после функции должно быть по 2 пустые строки;)
def summ(number):
    summa = 0
    for i in range(1, number + 1):
        summa += i
    return summa

def sum_number(number):
    summa_number = 0
    while number != 0:
        summa_number += number % 10
        number //= 10
    return summa_number

def numbers(number):
    count = 0
    while number != 0:
        count += 1
        number //= 10
    return count

print('По условию задачи')
print('Сумма чисел:', summ(number))
print('Кол-во цифр в числе:', numbers(number))
print('Разность суммы и кол-ва цифр:', summ(number) - numbers(number))

print()
print('===================')
print()

# TODO: В конце файла должна быть одна пустая строка:)
print('По примеру работы программы')
print('Сумма чисел:', sum_number(number))
print('Кол-во цифр в числе:', numbers(number))
print('Разность суммы и кол-ва цифр:', sum_number(number) - numbers(number))