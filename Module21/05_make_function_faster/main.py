def calculating_math_func(num, fact_dict):
    if num in fact_dict:
        result = fact_dict[num]
    else:
        for index in range(max(fact_dict) + 1, num + 1):
            fact_dict[index] = fact_dict[index - 1] * index
        result = fact_dict[num]
    result /= num ** 3
    result = result ** 10
    return result, fact_dict


factorial_dict = {1: 1}
while True:
    number = int(input('Введите число: '))
    num_and_tuple = calculating_math_func(number, factorial_dict)
    factorial_dict = num_and_tuple[1]
    print(num_and_tuple[0])
