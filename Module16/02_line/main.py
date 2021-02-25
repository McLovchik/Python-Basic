first_list = []

for i_number in range(160, 176 + 1, 2):
    first_list.append(i_number)


second_list = []

for i_number in range(162, 180 + 1, 3):
    second_list.append(i_number)

first_list.extend(second_list)

for i_min_num in range(len(first_list)):
    for i_act in range(i_min_num, len(first_list)):
        if first_list[i_act] < first_list[i_min_num]:
            first_list[i_act], first_list[i_min_num] = first_list[i_min_num], first_list[i_act]

print(first_list)
