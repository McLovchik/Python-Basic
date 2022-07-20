import os


def get_info(fun_path, total_size=0, count_dirs=0, count_files=0):
    if os.path.isfile(fun_path):
        count_files += 1
        size_file = os.path.getsize(fun_path)
        total_size += size_file
    else:
        for i_elem in os.listdir(fun_path):
            if not os.path.isfile((os.path.abspath(os.path.join(fun_path, i_elem)))):
                count_dirs += 1
                info = get_info(os.path.abspath(os.path.join(fun_path, i_elem)))
                total_size += info[0]
                count_dirs += info[1]
                count_files += info[2]
            elif os.path.isfile(i_elem):
                count_files += 1
                size_file = os.path.getsize(i_elem)
                total_size += size_file
    return total_size, count_dirs, count_files


path = os.path.abspath(os.path.join('..', '..', 'Module14'))
print(path)

path_info = get_info(path)
print('Размер каталога (в Кб):', path_info[0] / 1024)
print('Количество подкаталогов:', path_info[1])
print('Количество файлов:', path_info[2])

# файл os_info.txt как-то неправильно воспринимает, не могу понять что не так
