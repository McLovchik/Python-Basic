def out(guests):
    while True:
        name = input('Имя гостя: ')
        if guests.count(name) != 0:
            guests.remove(name)
            print('Пока,', name)
            break
        else:
            print('Такого гостя нет(')
            print('Try again!')


def entry(guests):
    name = input('Имя гостя: ')
    if len(guests) >= 6:
        print('Прости,', name, 'но мест нет.')
    else:
        guests.append(name)
        print('Привет,', name)


guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']

while True:
    print('Сейчас на вечеринке', len(guests), 'человек:', guests)
    answer = input('Гость пришёл или ушёл? ')
    if answer == 'пора спать':
        break
    elif answer == 'ушёл':
        out(guests)
    elif answer == 'пришёл':
        entry(guests)
    print()

print()
print('Вечеринка закончилась, все легли спать.')
