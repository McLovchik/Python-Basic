films = ['Крепкий орешек', 'Назад в будущее', 'Таксист',
         'Леон', 'Богемская рапсодия', 'Город грехов',
         'Мементо', 'Отступники', 'Деревня']
list_favorite = []

while True:
    favorite = input('Любимый фильм: ')
    count = 0
    # TODO: Предлагаю проверять на вхождение при помощи оператора "in":)
    # Не понял(
    for number in range(len(films)):
        if favorite == films[number]:
            list_favorite.append(films[number])
            count = 1
            break
    if count != 1:
        print('Ошибка. Такого фильма нет')
        break

print('Список любимых фильмов:', list_favorite)
