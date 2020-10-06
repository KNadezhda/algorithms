"""
Задание 1.
Выполните профилирование памяти в скриптах
Проанализировать результат и определить программы с
наиболее эффективным использованием памяти.

Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько
вариантов кода для одной и той же задачи. Можно взять задачи с курса Основ или с текущего курса Алгоритмов

Результаты анализа вставьте в виде комментариев к коду.
Также укажите в комментариях версию Python и разрядность вашей ОС.

ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО
"""
# версия python 3.8
# iMAC: 64-битный процессор


import sys
from memory_profiler import profile


@profile
def func_1():
    sum_ = 0
    num = int(input('Введите целое число: '))
    sum_ += sys.getsizeof(num)
    even, odd = 0, 0

    while num > 0:
        if num % 2 == 0:
            even += 1
        else:
            odd += 1
        num = num // 10

    sum_ += sys.getsizeof(even)
    sum_ += sys.getsizeof(odd)
    print(f"четных - {even}, нечетных - {odd}")
    print(f'размер num: {sys.getsizeof(num)}')
    print(f'размер even: {sys.getsizeof(even)}')
    print(f'размер odd: {sys.getsizeof(odd)}')
    print(f'размер обьекта: {sum_}')


func_1()
"""
Введите целое число: 345
четных - 1, нечетных - 2
размер num: 24
размер even: 28
размер odd: 28
размер обьекта: 84

Для запуска программы было выделено 10.5 MiB.
Т.к. мы не создавали списков нам понадобилось 0.0 MiB.
Line #    Mem usage    Increment   Line Contents
================================================
    25     10.5 MiB     10.5 MiB   @profile
    26                             def func_1():
    27     10.5 MiB      0.0 MiB       sum_ = 0
    28     10.5 MiB      0.0 MiB       num = int(input('Введите целое число: '))
    29     10.5 MiB      0.0 MiB       sum_ += sys.getsizeof(num)
    30     10.5 MiB      0.0 MiB       even, odd = 0, 0
    31                             
    32     10.5 MiB      0.0 MiB       while num > 0:
    33     10.5 MiB      0.0 MiB           if num % 2 == 0:
    34     10.5 MiB      0.0 MiB               even += 1
    35                                     else:
    36     10.5 MiB      0.0 MiB               odd += 1
    37     10.5 MiB      0.0 MiB           num = num // 10
    38                             
    39     10.5 MiB      0.0 MiB       sum_ += sys.getsizeof(even)
    40     10.5 MiB      0.0 MiB       sum_ += sys.getsizeof(odd)
    41     10.5 MiB      0.0 MiB       print(f"четных - {even}, нечетных - {odd}")
    42     10.5 MiB      0.0 MiB       print(f'размер num: {sys.getsizeof(num)}')
    43     10.5 MiB      0.0 MiB       print(f'размер even: {sys.getsizeof(even)}')
    44     10.5 MiB      0.0 MiB       print(f'размер odd: {sys.getsizeof(odd)}')
    45     10.5 MiB      0.0 MiB       print(f'размер обьекта: {sum_}')
"""


# 2 вариант


@profile
def recur_method(num1, even1=0, odd1=0):
    if num1 == 0:
        return even1, odd1
    else:
        num_1 = num1 % 10
        num1 = num1 // 10
        if num_1 % 2 == 0:
            even1 += 1
        else:
            odd1 += 1
        return recur_method(num1, even1, odd1)


try:
    NUM = int(input("Введите целое число: "))
    print(f"Количество четных и нечетных цифр: {recur_method(NUM)}")
except ValueError:
    print("введите число")

"""
Для запуска программы было выделено 10.4 MiB.
Т.к. мы не создавали списков нам понадобилось 0.0 MiB.
Line #    Mem usage    Increment   Line Contents
================================================
    54     10.4 MiB     10.4 MiB   @profile
    55                             def recur_method(num1, even1=0, odd1=0):
    56     10.4 MiB      0.0 MiB       if num1 == 0:
    57     10.4 MiB      0.0 MiB           return even1, odd1
    58                                 else:
    59     10.4 MiB      0.0 MiB           num_1 = num1 % 10
    60     10.4 MiB      0.0 MiB           num1 = num1 // 10
    61     10.4 MiB      0.0 MiB           if num_1 % 2 == 0:
    62     10.4 MiB      0.0 MiB               even1 += 1
    63                                     else:
    64     10.4 MiB      0.0 MiB               odd1 += 1
    65     10.5 MiB      0.0 MiB           return recur_method(num1, even1, odd1)

"""

# сложение цифр трехзначного числа


@profile
def func_2():
    sum_1 = 0
    num = input('Введите трехзначное число: ')
    sum_1 += sys.getsizeof(num)
    num2 = int(num)
    a = num2 // 100  # целочисленное деление"
    b = num2 % 100 // 10
    c = num2 % 10  # остаток от деления
    summa = a + b + c
    op = a * b * c
    sum_1 += sys.getsizeof(summa)
    sum_1 += sys.getsizeof(op)
    print(f'сума = {summa}')
    print(f'произведение = {op}')
    print(f'размер объекта: {sum_1}')


func_2()

"""
Введите трехзначное число: 345
сума = 12
произведение = 60
размер a: 34
размер b: 51
размер c: 21
размер объекта: 108
Для запуска программы было выделено 10.5 MiB.
Т.к. мы не создавали списков нам понадобилось 0.0 MiB.
Line #    Mem usage    Increment   Line Contents
================================================
   126     10.5 MiB     10.5 MiB   @profile
   127                             def func_2():
   128     10.5 MiB      0.0 MiB       sum_1 = 0
   129     10.5 MiB      0.0 MiB       num = input('Введите трехзначное число: ')
   130     10.5 MiB      0.0 MiB       sum_1 += sys.getsizeof(num)
   131     10.5 MiB      0.0 MiB       num2 = int(num)
   132     10.5 MiB      0.0 MiB       a = num2 // 100  # целочисленное деление"
   133     10.5 MiB      0.0 MiB       b = num2 % 100 // 10
   134     10.5 MiB      0.0 MiB       c = num2 % 10  # остаток от деления
   135     10.5 MiB      0.0 MiB       summa = a + b + c
   136     10.5 MiB      0.0 MiB       op = a * b * c
   137     10.5 MiB      0.0 MiB       sum_1 += sys.getsizeof(summa)
   138     10.5 MiB      0.0 MiB       sum_1 += sys.getsizeof(op)
   139     10.5 MiB      0.0 MiB       print(f'сума = {summa}')
   140     10.5 MiB      0.0 MiB       print(f'произведение = {op}')
   141     10.5 MiB      0.0 MiB       print(f'размер объекта: {sum_1}')
"""

# решение через цикл


@profile
def func_3():
    sum_2 = 0
    num = input('Введите трехзначное число: ')
    num3 = str(num)
    sum_2 += sys.getsizeof(num)
    summa = 0
    op = 1
    for i in num3:
        summa += int(i)
        op *= int(i)

    sum_2 += sys.getsizeof(summa)
    sum_2 += sys.getsizeof(op)
    print(f'сума = {summa}')
    print(f'произведение = {op}')
    print(f'размер объекта: {sum_2}')


func_3()

"""
сума = 12
произведение = 60
размер объекта: 108
Для запуска программы было выделено 10.5 MiB.
Т.к. мы не создавали списков нам понадобилось 0.0 MiB.
Line #    Mem usage    Increment   Line Contents
================================================
   159     10.5 MiB     10.5 MiB   @profile
   160                             def func_3():
   161     10.5 MiB      0.0 MiB       sum_2 = 0
   162     10.5 MiB      0.0 MiB       num = input('Введите трехзначное число: ')
   163     10.5 MiB      0.0 MiB       num3 = str(num)
   164     10.5 MiB      0.0 MiB       sum_2 += sys.getsizeof(num)
   165     10.5 MiB      0.0 MiB       summa = 0
   166     10.5 MiB      0.0 MiB       op = 1
   167     10.5 MiB      0.0 MiB       for i in num3:
   168     10.5 MiB      0.0 MiB           summa += int(i)
   169     10.5 MiB      0.0 MiB           op *= int(i)
   170                             
   171     10.5 MiB      0.0 MiB       sum_2 += sys.getsizeof(summa)
   172     10.5 MiB      0.0 MiB       sum_2 += sys.getsizeof(op)
   173     10.5 MiB      0.0 MiB       print(f'сума = {summa}')
   174     10.5 MiB      0.0 MiB       print(f'произведение = {op}')
   175     10.5 MiB      0.0 MiB       print(f'размер объекта: {sum_2}')
"""
