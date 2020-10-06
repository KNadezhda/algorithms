"""
Задача 3.
В соответствии с документацией Python,
deque – это обобщение стеков и очередей.
Вот основное правило: если вам нужно что-то быстро дописать или вытащить, используйте deque.
Если вам нужен быстрый случайный доступ, используйте list.

Задача: создайте простой список (list) и очередь (deque).
Выполните различные операции с каждым из объектов.
Сделайте замеры и оцените, насколько информация в документации
соответствует дейстивтельности.
"""

from collections import deque
import timeit


def time_testing(n):
    integer_list = list(range(n))
    integer_deque = deque(range(n))
    t_list = timeit.timeit(lambda: integer_list.append(0), number=n)
    t_deque = timeit.timeit(lambda: integer_deque.append(0), number=n)
    return f"{n: <9} list: {t_list:.10} | deque: {t_deque:.10}"


numbers = (100, 1000, 10000, 100000, 1000000, 10000000)
for number in numbers:
    print(time_testing(number))

# 100      list: 2.1054e-05 | deque: 1.8665e-05
# 1000     list: 0.00021706 | deque: 0.000171521
# 10000    list: 0.00176277 | deque: 0.001935606
# 100000   list: 0.018387374 | deque: 0.016496712
# 1000000  list: 0.161702444 | deque: 0.160632133
# 10000000 list: 1.601404474 | deque: 1.611392136
# с увеличением длинны списка функция append для list и deque выполняется одинаково по времени

list_with_range = [el for el in range(1000)]
deque_with_range = deque()
deque_with_range.extend(list_with_range)


def list_append(num):
    my_list = []
    for i in range(num):
        my_list.append(i)


def deque_append(num):
    my_list = deque()
    for i in range(num):
        my_list.append(i)


def list_appendleft(num):
    my_list = []
    for i in range(num):
        my_list.insert(0, i)


def deque_appendleft(num):
    my_list = deque()
    for i in range(num):
        my_list.appendleft(i)


def list_extend(lst_range):
    my_list = []
    my_list.extend(lst_range)


def deque_extend(lst_range):
    my_list = deque()
    my_list.extend(lst_range)


def list_extendleft(lst_range):
    my_list = []
    for el in lst_range:
        my_list.insert(0, el)


def deque_extendleft(lst_range):
    my_list = deque()
    my_list.extendleft(lst_range)


def list_pop(lst_range):
    for i in range(len(lst_range)):
        a = lst_range.pop()


def deque_pop(lst_range):
    for i in range(len(lst_range)):
        a = lst_range.pop()


def list_popleft(lst_range):
    for i in range(len(lst_range)):
        a = lst_range.pop(0)


def deque_popleft(lst_range):
    for i in range(len(lst_range)):
        a = lst_range.popleft()


def list_reverse(lst_range):
    a = lst_range.reverse()


def deque_reverse(lst_range):
    a = lst_range.reverse()


name_list = 'list_append deque_append list_appendleft deque_appendleft list_extend deque_extend list_extendleft deque_extendleft list_pop deque_pop list_popleft deque_popleft list_reverse deque_reverse'.split()

for id, func_name in enumerate(name_list):
    if id % 10 == 0:
        print()
    if id <= 3:
        print(f"{func_name}:\t{timeit.timeit(stmt=func_name + f'(1000)', setup=f'from __main__ import {func_name}', number=10000, globals=globals())}")
    else:
        if id % 10 == 0:
            print(f"{func_name}(list_with_range):\t{timeit.timeit(stmt=func_name + f'({list_with_range})', setup=f'from __main__ import {func_name}', number=10000, globals=globals())}")
        else:
            print(f"{func_name}(deque_with_range):\t{timeit.timeit(stmt=func_name + f'({deque_with_range})', setup=f'from __main__ import {func_name}', number=10000, globals=globals())}")

# list_append :	0.760536516
# deque_append :	0.7318628250000001 - append в данном случае отрабатывает с одинаковым временем
# list_appendleft :	2.938127087
# deque_appendleft :	0.7358613260000002 - appendleft с deque отрабатывает в несколько раз быстрее
# list_extend(deque_with_range) :	0.14824514299999958
# deque_extend(deque_with_range) :	0.18439731700000017 - extend в данном случае отрабатывает с примерно одинаковым временем
# list_extendleft(deque_with_range) :	2.918009883
# deque_extendleft(deque_with_range) :	0.18379827000000049 - extendleft с deque отрабатывает значительно быстрее
# list_pop(deque_with_range) :	0.763149931000001
# deque_pop(deque_with_range) :	0.7633407939999994 - pop в данном случае отрабатывает с примерно одинаковым временем

# list_popleft(list_with_range) -	1.7015503760000001
# deque_popleft(deque_with_range) -	0.7586464890000002 - popleft с deque отрабатывает в несколько раз быстрее
# list_reverse(deque_with_range) -	0.10699091300000063
# deque_reverse(deque_with_range) -	0.10785345400000068 - reverse в данном случае отрабатывает с примерно одинаковым временем


