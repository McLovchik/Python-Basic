players = {
    ("Ivan", "Volkin"): (10, 5, 13),
    ("Bob", "Robbin"): (7, 5, 14),
    ("Rob", "Bobbin"): (12, 8, 2)
}

players_list = list()

for i_name_surname, j_points in players.items():
    timely_tuple = tuple()
    for k_one in i_name_surname:
        timely_tuple += (k_one,)
    for l_point in j_points:
        timely_tuple += (l_point,)
    players_list.append(timely_tuple)

print(players_list)

# как сделать проще - эффективнее?
