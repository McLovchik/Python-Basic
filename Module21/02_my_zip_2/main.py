def my_zip(*args):
    min_length = min([len(elem) for elem in args])
    data = list(args)
    new_data = [tuple([sym[i_ind] for sym in data]) for i_ind in range(min_length)]
    return new_data


a = [{"x": 4}, "b", "z", "d", 5]
b = (10, {20}, [30], "z")
x = (1, 2, 3, 4, 5)

new_list = my_zip(a, b, x)

for i in new_list:
    print(i)
