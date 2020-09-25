"""
Задание 1.

Докажите, что словари обрабатываются быстрее, чем списки.

Реализуйте две функции, в первой нужно заполнить элементами список, во второй-словарь
Сделайте замеры времени выполнения каждой из функций

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)

Примечание: eсли вы уже знаете, что такое декоратор и как его реализовать,
то реализуйте ф-цию-декоратор и пусть она считает время
И примените ее к двум своим функциям.
"""

import time


def time_test(function):  # функция-декоратор
    def paper(*args):
        start = time.time()
        function(args[0])
        end = time.time()
        print('Время выполнения: {} секунд.'.format(end - start))  # print(end - start)
    return paper


@time_test  # декоратор
def list_mas(n):
    list_obj = []
    for i in range(n):
        list_obj.append(i)
        list_obj.index(i)
    return list_mas


@time_test
def dict_mas(n):
    dict_obj = dict()
    for i in range(n):
        dict_obj[i] = i
        dict_obj.get(i)
    return dict_mas


list_mas(1000)
dict_mas(1000)
