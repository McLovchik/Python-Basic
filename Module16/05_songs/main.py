violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]

special_playlist = []

songs = int(input('Сколько песен выбрать? '))
time = 0

# TODO: Аналогично 3;)
for i_num in range(1, songs + 1):
    song = input(f'Название {i_num} песни: ')
    for i_element in violator_songs:
        if i_element[0] == song:
            time += i_element[1]

print()
print('Общее время звучания песен: ', time, 'минут')
