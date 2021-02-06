video_cards = int(input('Кол-во видеокарт: '))
old_list_cards = []
new_list_cards = []
max_age = 0

for number in range(1, video_cards + 1):
    print(number, 'Видеокарта:', end=' ')
    age = int(input())
    if age > max_age:
        max_age = age
    old_list_cards.append(age)

for number in range(video_cards):
    if old_list_cards[number] != max_age:
        new_list_cards.append(old_list_cards[number])

print('Старый список видеокарт: ', old_list_cards)
print('Новый список видеокарт: ', new_list_cards)
