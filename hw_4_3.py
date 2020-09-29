"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через cProfile и через timeit

Сделайте вывод, какая из трех реализаций эффективнее и почему
"""

import timeit
import cProfile


def revers(enter_num, revers_num=0):
    if enter_num == 0:
        return
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        revers(enter_num, revers_num)


def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


enter_num = int(input('Введите целое число: '))  # 345678
revers(enter_num, revers_num=0)
revers_2(enter_num, revers_num=0)
revers_3(enter_num)
print(timeit.timeit('revers(enter_num)', number=100, globals=globals()))  # 0.00024298199999961412
print(timeit.timeit('revers_2(enter_num)', number=100, globals=globals()))  # 0.00012516399999995542
print(timeit.timeit('revers_3(enter_num)', number=100, globals=globals()))  # 5.164099999976912e-05

"""
срез является самым быстрым из 3-х решений
"""

cProfile.run('revers(345678)')  # 7/1    0.000    0.000    0.000    0.000 hw_4_3.py:18(revers)
"""
рекурсия для решения совершает стек 7 раз, соответственно она самая медленная
"""
cProfile.run('revers_2(345678)')  # 1    0.000    0.000    0.000    0.000 hw_4_3.py:28(revers_2)
cProfile.run('revers_3(345678)')  # 1    0.000    0.000    0.000    0.000 hw_4_3.py:36(revers_3)
