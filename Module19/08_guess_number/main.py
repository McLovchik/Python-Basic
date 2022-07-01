max_num = int(input('Введите максимальное число: '))

nums_set = set(list(range(1, max_num + 1)))
# sought_set = set()

while True:
    trial_list = input('Нужное число есть среди вот этих чисел: ')
    if trial_list == 'Помогите!':
        print(f'Артём мог загадать следующие числа: {nums_set}')
        break
    trial_list = trial_list.split(' ')
    trial_list = list(map(int, trial_list))
    trial_set = set(trial_list)
    answer = input('Ответ Артёма: ')
    if answer == 'Да':
        nums_set &= trial_set
    elif answer == 'Нет':
        nums_set -= trial_set
