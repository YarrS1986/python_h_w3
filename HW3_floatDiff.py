# Задайте список из вещественных чисел. Напишите программу, которая найдёт
# разницу между максимальным и минимальным значением дробной части элементов.
#         [1.1, 1.2, 3.1, 5, 10.01] => 0.19

def find_maximum_remains(my_list):
    max_remains = round(my_list[0] - int(my_list[0]), 10)
    for i in range(len(my_list)):
        my_list[i] = round(my_list[i] - int(my_list[i]), 10)
        if max_remains < my_list[i] and my_list[i] != 0:
            max_remains = my_list[i]
    return max_remains

def find_minimum_remains(my_list):
    min_remains = round(my_list[0] - int(my_list[0]), 10)
    for i in range(len(my_list)):
        my_list[i] = round(my_list[i] - int(my_list[i]), 10)
        if min_remains > my_list[i] and my_list[i] != 0:
            min_remains = my_list[i]
    return min_remains

list_len = int(input('Введи длину списка = '))
list = [float(input(f'Введи {i} элемент списка -> ').replace(",", ".")) for i in range(list_len)]

print(f'{list} -> {find_maximum_remains(list) - find_minimum_remains(list)}')