word = input('Введите слово: ')
symbols = list(word)
letters = len(symbols)
left_part_of_word = []
right_part_of_word = []

if letters % 2 == 1:
    limit = letters // 2
else:
    limit = letters // 2 - 1

for index in range(0, letters // 2, 1):
    left_part_of_word.append(symbols[index])

for index in range(letters - 1, limit, -1):
    right_part_of_word.append(symbols[index])

count = 0
for index in range(letters // 2):
    if left_part_of_word[index] == right_part_of_word[index]:
        count += 1

if count == letters // 2:
    print('Слово является палиндромом')
else:
    print('Слово не является палиндромом')
