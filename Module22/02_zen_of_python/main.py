readable_file = open('zen.txt', 'r')
data = readable_file.read()

data_list = data.split('\n')

for i_str in reversed(data_list):
    print(i_str)

readable_file.close()
