number = int(input('Введите число: '))

answer = [(1 if i_index % 2 == 0
           else i_index % 5)
          for i_index in range(number)]

print(answer)
