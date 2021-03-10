text = input('Введите текст: ')
vowels = ['a', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я',
          'А', 'Е', 'Ё', 'И', 'О', 'У', 'Ы', 'Э', 'Ю', 'Я']

answer_vowels = [letter_text
                 for letter_text in text
                 if letter_text in vowels]

print('Список гласных букв:', answer_vowels)
print('Длина списка:', len(answer_vowels))
