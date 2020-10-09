"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.

Пример:
Введите число элементов: 5
Исходный - [46.11436617832828, 41.62921998361278, 18.45859540989644, 12.128870723745806, 8.025098788570562]
Отсортированный - [8.025098788570562, 12.128870723745806, 18.45859540989644, 41.62921998361278, 46.11436617832828]
"""
import random
import timeit


def merge_sort(array):
    if len(array) <= 1:
        return array
    center = len(array) // 2
    left = array[:center]
    right = array[center:]
    merge_sort(left)
    merge_sort(right)
    i = j = 0

    while len(left) > i and len(right) > j:
        if left[i] < right[j]:
            array[i + j] = left[i]
            i += 1
        else:
            array[i + j] = right[j]
            j += 1

    while len(left) > i:
        array[i + j] = left[i]
        i += 1
    while len(right) > j:
        array[i + j] = right[j]
        j += 1

    return array


data = [random.uniform(0, 50) for _ in range(5)]
print(timeit.timeit("merge_sort(data[:])", setup="from __main__ import  merge_sort, data", number=10))
print(f'Исходный: {data}')
print(f'Отсортированный: {merge_sort(data)}')

# 8.657499999999846e-05

"""
data1 = [round(random.uniform(0, LIMIT), 2) for _ in range(SIZE)] 
print(data1)
print(merge_sort(data1))
"""