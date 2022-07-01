count = int(input('Введите количество пар слов: '))

synonyms = dict()

for count in range(1, count + 1):
    pair = input(f'{count} пара: ').split(' - ')
    synonyms[pair[0]] = pair[1]

while True:
    word = input('Введите слово: ')
    count = 0
    for key in synonyms:
        if key.capitalize() == word.capitalize():
            print(f'Синоним: {synonyms[key]}')
            count += 1
            break
        elif synonyms[key].capitalize() == word.capitalize():
            print(f'Синоним: {key}')
            count += 1
            break
    if count == 0:
        print('Такого слова в словаре нет.')
