def interests_and_len_surnames(students_dict):
    interests_list = list()
    string_surnames = ''
    for j_id in students_dict:
        interests_list += (students_dict[j_id]['interests'])
        string_surnames += students_dict[j_id]['surname']
    return interests_list, len(string_surnames)


students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology', 'swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}

id_age = list()
for i_id in students:
    id_age_list = (i_id, students[i_id]['age'])
    id_age_tuple = tuple(id_age_list)
    id_age.append(id_age_tuple)

interests = interests_and_len_surnames(students)[0]
len_surnames = interests_and_len_surnames(students)[1]

print('Список пар "ID студента — возраст":', id_age)
print('Полный список интересов всех студентов:', interests)
print('Общая длина всех фамилий студентов:', len_surnames)
