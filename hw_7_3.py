"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы.

Задачу можно решить без сортировки исходного
массива.

Но если это слишком сложно, то используйте метод сортировки,
который не рассматривался на уроках: Шелла, Гномья, ...

arr[m]
from statistics import median
"""

import timeit
import random
import statistics


def my_sort(lst_obj):
    trans = lst_obj
    right_list = []
    left_list = []
    for i in range(len(trans)):
        for j in range(len(trans)):
            if trans[i] > trans[j]:
                left_list.append(trans[j])
            if trans[i] < trans[j]:
                right_list.append(trans[i])
            if trans[i] == trans[j] and i > j:
                left_list.append(trans[j])
            if trans[i] == trans[j] and i < j:
                right_list.append(trans[i])
        if len(left_list) == len(right_list):
            return trans[i]
        left_list.clear()
        right_list.clear()


m = int(input('введите m: '))
orig_list = [random.randint(0, 50) for _ in range(2 * m + 1)]
print(f'массив:{orig_list}')
print(f'медиана: {my_sort(orig_list)}')
print(sorted(orig_list))  # отсортированный массив
print(timeit.timeit("my_sort(orig_list[:])", setup="from __main__ import my_sort, orig_list", number=1))
print(f'медиана = {statistics.median(orig_list)}')
print(sorted(orig_list))
