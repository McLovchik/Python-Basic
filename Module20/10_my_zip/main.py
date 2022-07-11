def short_seq(string, tpl):
    return min(len(string), len(tpl))


syms_str = 'abcd'
nums_tpl = (10, 20, 30, 40)

pairs = (
    (syms_str[i_elem], nums_tpl[i_elem])
    for i_elem in range(short_seq(syms_str, nums_tpl))
)
print(pairs)

for j_elem in pairs:
    print(j_elem)
