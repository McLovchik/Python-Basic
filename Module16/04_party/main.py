guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']


while True:
    print('Сейчас на вечеринке', len(guests), 'человек:', guests)
    answer = input('Гость пришёл или ушёл? ')
    if answer == 'пора спать':
        break
    elif answer == 'ушёл':
        name = input('Имя гостя: ')
        guests.remove(name)
        print('Пока,', name)
    elif answer == 'пришёл':
        name = input('Имя гостя: ')
        if len(guests) >= 6:
            print('Прости,', name, 'но мест нет.')
        else:
            guests.append(name)
            print('Привет,', name)
    print()

print()
print('Вечеринка закончилась, все легли спать.')
