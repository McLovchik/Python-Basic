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

for i_num in range(1, songs + 1):
    song = input(f'Название {i_num} песни: ')
    for i_index in range(0, len(violator_songs)):
        if violator_songs[i_index][0] == song:
            time += violator_songs[i_index][1]

print()
print('Общее время звучания песен: ', time, 'минут')