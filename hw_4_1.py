"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры

Добавьте аналитику: что вы сделали и почему
"""

import timeit


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_2(nums):
    return [i for i, el in enumerate(nums) if not el % 2]


NUMS = [el for el in range(1000)]

print(timeit.timeit('func_1(NUMS)', number=100, globals=globals()))  # 0.012966294
print(timeit.timeit('func_2(NUMS)', number=100, globals=globals()))  # 0.009186165000000003


# цикл for работает медленнее чем генераторное выражение
# линейная сложность, с увеличением числа растет время исполнения функции


"""
from random import random
N = 10
arr = [0]*N
even = []
for i in range(N):
    arr[i] = int(random() * 10) + 10
    if arr[i] % 2 == 0:
        even.append(i)
print(arr)
print('Индексы четных элементов: ', even)
"""