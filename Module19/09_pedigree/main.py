people = int(input('Введите количество человек: '))
gen_dict = dict()
gen_pairs = dict()

for i_pair in range(1, people):
    pair = input(f'{i_pair} пара: ').split(' ')
    gen_pairs[pair[0]] = pair[1]

for i_key in gen_pairs:
    count = 0
    if gen_pairs[i_key] not in gen_dict:
        gen_dict[gen_pairs[i_key]] = 0
    man = i_key
    while True:
        if man in gen_pairs.values():
            count += 1
            man = gen_pairs[man]  # = ключу
        else:
            gen_dict[i_key] = count
            break

print(gen_dict)

# не доделал
