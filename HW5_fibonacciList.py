# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# k = 8: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

def fib(n):
    if n in [-1, 1, 2]:
        return 1
    elif n == 0:
        return 0
    elif n == -2:
        return -1
    elif n < -2:
        return fib(n + 2) - fib(n + 1)
    else:
        return fib(n - 1) + fib(n - 2)


k = int(input('Введи целочисленное число = '))
list = []
for e in range(-k, k + 1):
    list.append(fib(e))

print(f'k = {k}: {list}')