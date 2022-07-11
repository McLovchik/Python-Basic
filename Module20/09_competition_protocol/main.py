count_records = int(input('Сколько записей вносится в протокол? '))
records = dict()

print('Записи (результат и имя):')
var_record = 0
for i_record in range(1, count_records + 1):
    record = input(f'{i_record}-я запись: ').split()
    if record[1] in records.keys():
        if records[record[1]][0] < int(record[0]):
            records[record[1]] = [int(record[0]), i_record]
    else:
        records[record[1]] = [int(record[0]), i_record]

for i_place in range(1, 4):
    max_num = 0
    for i_keys in records.keys():
        if records[i_keys][0] > max_num:
            max_num = records[i_keys][0]
            record_max_num = records[i_keys][1]
            name_max_num = i_keys
        elif records[i_keys][0] == max_num:
            if record_max_num > records[i_keys][1]:
                record_max_num = records[i_keys][1]
                name_max_num = i_keys
    print(f'{i_place}-е место. {name_max_num} ({max_num})')
    records.pop(name_max_num)
