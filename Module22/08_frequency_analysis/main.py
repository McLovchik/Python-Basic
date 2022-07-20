import os

alphabet = 'abcdefghijklmnopqrstuvwxyz'
name_text_file = 'text.txt'
path_to_text_file = os.path.abspath(name_text_file)
file_contents = open(path_to_text_file, 'r')
data = file_contents.read().lower()

analysis_dict = {}
count_syms = 0
for i_sym in data:
    if i_sym in alphabet:
        count_syms += 1
        if i_sym not in analysis_dict:
            analysis_dict[i_sym] = 1
        else:
            analysis_dict[i_sym] += 1

for i_sym in analysis_dict:
    analysis_dict[i_sym] = round(analysis_dict[i_sym] / count_syms, 3)

sorted_alpha_list = sorted(analysis_dict)
sorted_alpha_dict = dict()
for i_key in sorted_alpha_list:
    sorted_alpha_dict[i_key] = analysis_dict[i_key]

sorted_analysis_dict = dict()
sorted_keys = sorted(sorted_alpha_dict, key=sorted_alpha_dict.get, reverse=True)

for i in sorted_keys:
    sorted_analysis_dict[i] = sorted_alpha_dict[i]

path_to_analysis_file = os.path.abspath(os.path.join(path_to_text_file, '..', 'analysis.txt'))
analysis_file = open(path_to_analysis_file, 'w')

for i_elem in sorted_alpha_dict:
    our_str = i_elem + ' ' + str(sorted_alpha_dict[i_elem]) + '\n'
    analysis_file.write(our_str)

file_contents.close()
analysis_file.close()
