text = input('Введите строку: ').split()

max_elem = text[0]
for element in text:
    if len(max_elem) < len(element):
        max_elem = element

print(max_elem, len(max_elem))
