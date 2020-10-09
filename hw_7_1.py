"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы. Сортировка должна быть реализована в
виде функции. Обязательно доработайте алгоритм (сделайте его умнее).

Идея доработки: если за проход по списку не совершается ни одной сортировки,
то завершение
Обязательно сделайте замеры времени обеих реализаций
и обосновать дала ли оптимизация эффективность

Подсказка: обратите внимание, сортируем не по возрастанию, как в примере,
а по убыванию
"""
# версия python 3.8
# iMAC: 64-битный процессор

import timeit
import random


def bubble_sort(lst_obj):
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj)-n):
            if lst_obj[i] < lst_obj[i+1]:
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
        n += 1
    return lst_obj


def bubble_sort_1(lst_obj):
    n = 1
    while n < len(lst_obj):
        in_sorted = True
        for i in range(len(lst_obj)-n):
            if lst_obj[i] < lst_obj[i+1]:
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
                in_sorted = False
        if in_sorted:
            break

        n += 1
    return lst_obj


orig_list = [random.randint(-100, 100) for _ in range(1000)]
print(timeit.timeit("bubble_sort(orig_list[:])", setup="from __main__ import  bubble_sort, orig_list", number=10))
print(timeit.timeit("bubble_sort_1(orig_list[:])", setup="from __main__ import  bubble_sort_1, orig_list", number=10))
print(orig_list)
print(bubble_sort(orig_list))
print(bubble_sort_1(orig_list))
"""
время обработки почти одинаковое
0.980550187
0.9757900749999999
"""