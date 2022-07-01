def comp_gen_tree(amount):
    childs_parents = dict()
    count = 0
    while True:
        count += 1
        child_parent = input(f'{count} пара: ').split()
        if child_parent[1] not in childs_parents:
            childs_parents.setdefault(child_parent[1], 0)
            childs_parents.setdefault(child_parent[0], 1)
        elif childs_parents[child_parent[1]] == 0:
            childs_parents[child_parent[0]] = 1
        else:
            childs_parents[child_parent[0]] = childs_parents[child_parent[1]] + 1

        if len(childs_parents) >= amount:
            break

    return childs_parents


amount_people = int(input('Введите количество человек: '))
var_height_man = comp_gen_tree(amount_people)
height_man = sorted(var_height_man.keys())
print(height_man)
#
print('“Высота” каждого члена семьи:')
#
for human in height_man:
    height = var_height_man.get(human)
    print(f'{human}: {height}')
