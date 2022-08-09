def hofstadter_q_sequence_generator(user_sequence: list):
    sequence = user_sequence[:]
    if sequence == [1, 1]:
        yield 1
        yield 1
        while True:
            next_value = sequence[(len(sequence) + 1 - sequence[len(sequence) - 1]) - 1] + \
                         sequence[(len(sequence) + 1 - sequence[len(sequence) - 2]) - 1]
            sequence.append(next_value)
            yield next_value
    else:
        raise ValueError('Введена неверная последовательность')


user_count_nums = int(input('Введите кол-во первых членов последовательности, которые вы хотите увидеть: '))

hofstadter_q_sequence = hofstadter_q_sequence_generator([1, 1])
hofstadter_q_sequence_list = [next(hofstadter_q_sequence) for _ in range(user_count_nums)]
print('Последовательность Q Хофштадтера:', hofstadter_q_sequence_list)
