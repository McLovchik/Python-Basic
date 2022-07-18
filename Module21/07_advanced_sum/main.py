def my_sum(*args):
    def flatten(args_list):
        summa = []
        for elem in args_list:
            if isinstance(elem, int):
                summa.append(elem)
            else:
                summa.extend(flatten(elem))
        return summa
    return sum(flatten(args))


print(my_sum(1, 2, 3, 4, 5))
# print(my_sum([[1, 2, [3]], [1], 3]))
