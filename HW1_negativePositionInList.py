# Задайте список из нескольких чисел.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

list_len = int(input('Введи длину списка = '))
list = []
sum_negative_position = 0
for i in range(list_len):
    list.append(int(input(f'Введи {i} элемент списка -> ')))
    if i % 2 != 0:
        sum_negative_position += list[i]

print(list, 'ответ:', sum_negative_position)