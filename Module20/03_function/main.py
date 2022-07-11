def slicer(fun_tuple, fun_element):
    new_tuple = tuple()
    if fun_element in fun_tuple:
        count = fun_tuple.count(fun_element)
        if count == 1:
            new_tuple = fun_tuple[fun_tuple.index(fun_element):]
        else:
            left_index = fun_tuple.index(fun_element)
            right_index = fun_tuple[left_index + 1:].index(fun_element) + left_index + 1
            new_tuple = fun_tuple[left_index:right_index + 1]
    return new_tuple


our_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 2, 2, 9, 10)
our_element = 2
print(slicer(our_tuple, our_element))
