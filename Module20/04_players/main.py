players = {
    ("Ivan", "Volkin"): (10, 5, 13),
    ("Bob", "Robbin"): (7, 5, 14),
    ("Rob", "Bobbin"): (12, 8, 2)
}

players_list = [
    (i_name_surname + j_points)
    for i_name_surname, j_points in players.items()
]

print(players_list)
