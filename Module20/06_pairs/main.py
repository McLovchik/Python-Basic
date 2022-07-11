import random

original_list = [
    random.randint(1, 10)
    for _ in range(10)
]

print('Оригинальный список:', original_list)

new_list = zip(original_list[::2], original_list[1::2])

print('Новый список:')

for i_tuple in new_list:
    print(i_tuple)

# Оригинальный список: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# Новый список: [(0, 1), (2, 3), (4, 5), (6, 7), (8, 9)]
