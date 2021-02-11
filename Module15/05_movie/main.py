films = ['Крепкий орешек', 'Назад в будущее', 'Таксист',
         'Леон', 'Богемская рапсодия', 'Город грехов',
         'Мементо', 'Отступники', 'Деревня']
list_favorite = []

while True:
    favorite = input('Любимый фильм: ')
    count = 0
    # TODO: Предлагаю проверять на вхождение при помощи оператора "in":)
    for number in range(len(films)):
        if favorite == films[number]:
            list_favorite.append(films[number])
        else:
            count += 1
    # TODO: Не совсем очевиден смысл конструкции ниже:)
    if len(films) - count != 1:
        break

print('Ошибка. Такого фильма нет')
print('Список любимых фильмов:', list_favorite)
