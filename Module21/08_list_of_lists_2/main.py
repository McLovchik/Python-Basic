nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]], [[11, 12, 13], [14, 15], [16, 17, 18]]]


def disclosure(fun_list):
    if not fun_list:
        return []
    return disclosure(fun_list[:-1]) + (
        [fun_list[-1]]
        if not isinstance(fun_list[-1], list)
        else disclosure(fun_list[-1])
    )


print(disclosure(nice_list))
