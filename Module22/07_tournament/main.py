import os

name_first_file = 'first_tour.txt'
path_to_first_file = os.path.abspath(name_first_file)
file_contents = open(path_to_first_file, 'r')
data = file_contents.read()
data_list = data.split('\n')
min_points = int(data_list[0])
del data_list[0]

members_dict = {}
for i_member in data_list:
    split_str = i_member.split()
    members_dict[int(split_str[2])] = split_str[1][0] + '. ' + split_str[0]


points_list = sorted(members_dict)
while True:
    if points_list[0] < min_points + 1:
        del points_list[0]
    else:
        break

len_points_list = str(len(points_list)) + '\n'


path_to_second_file = os.path.abspath(os.path.join(path_to_first_file, '..', 'second_tour.txt'))
second_file = open(path_to_second_file, 'w')
second_file.write(len_points_list)

count = 0
for i_point in reversed(points_list):
    count += 1
    new_str = str(count) + ') ' + members_dict[i_point] + ' ' + str(i_point) + '\n'
    second_file.write(new_str)

file_contents.close()
second_file.close()
