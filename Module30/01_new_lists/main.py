from typing import List
from functools import reduce

floats: List[float] = [12.3554, 4.02, 5.777, 2.12, 3.13, 4.44, 11.0001]
names: List[str] = ["Vanes", "Alen", "Jana", "William", "Richards", "Joy"]
numbers: List[int] = [22, 33, 10, 6894, 11, 2, 1]

new_floats = [round(num ** 3, 3) for num in floats]
new_names = list(filter(lambda i_str: len(i_str) >= 5, names))
# new_names = [i_str for i_str in names if len(i_str) >= 5]
new_numbers = reduce(lambda prev, el: prev * el, numbers)

# print(new_floats)
# print(new_names)
# print(new_numbers)
