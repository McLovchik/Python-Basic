def conclusion(end_tuple):
    if is_int(end_tuple):
        new_tuple = tuple(sorted(end_tuple))
        print(new_tuple)
    else:
        print(end_tuple)


def is_int(check_tuple):
    for i_num in check_tuple:
        if i_num % int(i_num) != 0:
            return False
    return True


our_tuple = (6, 3, -1, 8, 4, 10, -5)

conclusion(our_tuple)
