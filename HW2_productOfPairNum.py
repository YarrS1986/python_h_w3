# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# - [2, 3, 4, 5, 6] => [12, 15, 16];         - [2, 3, 5, 6] => [12, 15]

lst_len = int(input('Введи длину списка = '))
lst = [int(input(f'Введи {i} элемент списка -> ')) for i in range(lst_len)]

calculate_lst = []
if len(lst) % 2 > 0:
    for i in range((len(lst) // 2) + 1):
        calculate_lst.append(lst[i] * lst[-1 - i])
else:
    for i in range(len(lst) // 2):
        calculate_lst.append(lst[i] * lst[-1 - i])

print(lst, '=>', calculate_lst)