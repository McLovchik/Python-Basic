readable_file = open('numbers.txt', 'r')
data = readable_file.read()
nums_sum = 0

for i_str in data:
    for i_elem in i_str:
        if i_elem.isdigit():
            nums_sum += int(i_elem)

print('Содержимое файла answer.txt')
print(nums_sum)

readable_file.close()
