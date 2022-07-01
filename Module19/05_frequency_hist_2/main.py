def histogram(string):
    sym_dict = dict()
    for sym in string:
        if sym in sym_dict:
            sym_dict[sym] += 1
        else:
            sym_dict[sym] = 1
    return sym_dict


text = input('Введите текст: ')
hist = histogram(text)
print('Оригинальный словарь частот:')
for i_key in hist:
    print(f'{i_key} : {hist[i_key]}')

print()
print('Инвертированный словарь частот:')

inv_hist = dict()

for i_key in hist:
    if hist[i_key] not in inv_hist:
        inv_hist[hist[i_key]] = list()
        inv_hist[hist[i_key]].append(i_key)
    else:
        inv_hist[hist[i_key]].append(i_key)

for i_key in inv_hist:
    print(f'{i_key} : {inv_hist[i_key]}')
