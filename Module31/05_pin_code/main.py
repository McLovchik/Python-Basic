import itertools

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for i_number in itertools.permutations(numbers, 4):
    print(i_number)
