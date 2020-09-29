"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Попытайтесь написать третью версию, которая будет самой быстрой.
Сделайте замеры и опишите, получилось ли у вас ускорить задачу.
"""

import timeit
import cProfile


def func_1():
    m = 0
    num = 0
    for i in array:
        count = array.count(i)
        if count > m:
            m = count
            num = i
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'


def func_2():
    new_array = []
    for el in array:
        count2 = array.count(el)
        new_array.append(count2)

    max_2 = max(new_array)
    elem = array[new_array.index(max_2)]
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_2} раз(а)'


def func_3():
    numb = max(array, key=array.count)
    return f"Чаще всего встречается число {numb}, оно появилось в массиве {array.count(numb)} раз(а)"


array = [14, 20, 4, 12, 7, 7, 14, 16, 20, 18, 20, 20, 10, 17, 4, 5, 5, 17, 3, 5]

print(func_1())
print(func_2())
print(func_2())
print(timeit.timeit('func_1()', number=100, globals=globals()))  # 0.0009205619999999998
print(timeit.timeit('func_2()', number=100, globals=globals()))  # 0.001104723000000002
print(timeit.timeit('func_3()', number=100, globals=globals()))  # 0.0008660210000000015

cProfile.run('func_1()')  # 20    0.000    0.000    0.000    0.000 {method 'count' of 'list' objects}
cProfile.run('func_2()')  # 20    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
# 20    0.000    0.000    0.000    0.000 {method 'count' of 'list' objects}
"""
func_2 самый долгий, т.к. формируется новый массив и уже в нем ищется max
"""

cProfile.run('func_3()')  # 1    0.000    0.000    0.000    0.000 {built-in method builtins.max}
"""
func_3 самый быстрый, т.к. ищем в массиве по ключу
"""
