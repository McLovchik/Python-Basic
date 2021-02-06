word = input('Введите слово: ')
unique = []

for check_letter in word:
    count = 0
    for letter in word:
        if check_letter == letter:
            count += 1
    if count == 1:
        unique.append(check_letter)

print('Кол-во уникальных букв:', len(unique))
