text = input('Введите текст: ')
vowels = ['a', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я',
          'А', 'Е', 'Ё', 'И', 'О', 'У', 'Ы', 'Э', 'Ю', 'Я']

# TODO: Предлагаю подумать как сделать проще:)
answer_vowels = [letter_vowels for letter_text in text for letter_vowels in vowels if letter_vowels == letter_text]

print('Список гласных букв:', answer_vowels)
print('Длина списка:', len(answer_vowels))
