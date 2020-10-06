"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните различные операции с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.
"""
from collections import OrderedDict
import timeit
import random


def operate_on_dict(g):
    test_dict = {}
    for key in range(g):
        test_dict[key] = random.random()


def operate_on_ordered_dict(g):
    test_ordered_dict = OrderedDict()
    for key in range(g):
        test_ordered_dict[key] = random.random()


print(timeit.timeit("operate_on_dict(1000)", number=1000, globals=globals()))  # 0.17828190400000002
print(timeit.timeit("operate_on_ordered_dict(1000)", number=1000, globals=globals()))  # 0.21587979999999998
# OrderedDict выполняется дольше dict, с увеличение словаря разрыв во времени увеличивается.
# вывод: dict работает быстрее
