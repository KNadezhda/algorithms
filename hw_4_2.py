"""
Задание 2.

Приведен код, который формирует из введенного числа
обратное по порядку входящих в него цифр.
Задача решена через рекурсию

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры

Подсказка: примените мемоизацию

Добавьте аналитику: что вы сделали и почему
"""

import timeit
from random import randint


def recursive_reverse(number):
    if number == 0:
        return str(number % 10)
    return f'{str(number % 10)}{recursive_reverse(number // 10)}'


x_100 = randint(1000, 10000)
x_1000 = randint(10000, 100000)
x_10000 = randint(1000000, 10000000)
print(x_100)
print(x_1000)
print(x_10000)
print(timeit.timeit('recursive_reverse(x_100)', number=100, globals=globals()))  # 0.00026855699999999913
print(timeit.timeit('recursive_reverse(x_1000)', number=100, globals=globals()))  # 0.000317946000000003
print(timeit.timeit('recursive_reverse(x_10000)', number=100, globals=globals()))  # 0.00040513399999999797

"""
время увеличивается с увеличением числа
"""

# мемоизация
# сохраняем промежуточное значение в словарь и больше пользуемся базовым случаем
# линейная зависимость


def memoize(f):
    recursive_d = {}

    def _recursive_dict(*args):
        if args in recursive_d:
            return recursive_d[args]
        else:
            recursive_d[args] = f(*args)
        return recursive_d[args]
    return _recursive_dict


@memoize
def recursive_dict(number):
    if number == 0:
        return ''
    return f'{str(number % 10)}{recursive_dict(number // 10)}'


print(timeit.timeit('recursive_dict(x_100)', number=100, globals=globals()))  # 3.703600000000071e-05
print(timeit.timeit('recursive_dict(x_1000)', number=100, globals=globals()))  # 3.42870000000009e-05
print(timeit.timeit('recursive_dict(x_10000)', number=100, globals=globals()))  # 3.855999999999998e-05

"""
время исполнения практически не увеличиваетя
"""