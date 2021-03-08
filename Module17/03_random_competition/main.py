import random

first_team = [round(random.uniform(5, 10), 2) for _ in range(20)]
print(first_team)

second_team = [round(random.uniform(5, 10), 2) for _ in range(20)]
print(second_team)

winners = [(first_team[i_index] if first_team[i_index] >= second_team[i_index]
            else second_team[i_index]) for i_index in range(20)]
print(winners)
