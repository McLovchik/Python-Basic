films = ['Крепкий орешек', 'Назад в будущее', 'Таксист',
         'Леон', 'Богемская рапсодия', 'Город грехов',
         'Мементо', 'Отступники', 'Деревня']
list_favorite = []

while True:
    favorite = input('Любимый фильм: ')
    if favorite in films:
        list_favorite.append(favorite)
    else:
        print('Ошибка. Такого фильма нет')
        break

print('Список любимых фильмов:', list_favorite)
