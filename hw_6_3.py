"""
Задание 3 *.
Сделать профилировку для скриптов с рекурсией и сделать,
можно так профилировать и есть ли 'подводные камни'
"""
from memory_profiler import profile


@profile
def arc():

    tag = input("Введите знак (+,-,*,/, или 0 для выхода): ")

    if tag == '0':
        print('выход')
    else:
        if tag in {'+', '-', '*', '/'}:
            x = float(input("x = "))
            y = float(input("y = "))
            if tag == '+':
                print(f'{x + y:.2f}')
            elif tag == '-':
                print(f'{x - y:.2f}')
            elif tag == '*':
                print(f'{x * y:.2f}')
            elif y != 0:
                print(f'{x / y:.2f}')
            else:
                print("Делить на ноль нельзя!")
            return arc()  # ретерн вынесен за if
        else:
            print("Знак операции введен неверно!")
            return arc()


arc()


@profile
def func():
    while True:
        tag = input("Введите знак (+,-,*,/, или 0 для выхода): ")
        if tag == '0':
            break
        else:
            if tag in {'+', '-', '*', '/'}:
                x = float(input("x = "))
                y = float(input("y = "))
                if tag == '+':
                    print(f'{x + y:.2f}')
                elif tag == '-':
                    print(f'{x - y:.2f}')
                elif tag == '*':
                    print(f'{x * y:.2f}')
                elif y != 0:
                    print(f'{x / y:.2f}')
                else:
                    print("Делить на ноль нельзя!")
            else:
                print("Знак операции введен неверно!")


func()

"""
и в первом и во втором случает выделяется 10.4 MiB
не требует оптимизации
Line #    Mem usage    Increment   Line Contents
================================================
     9     10.4 MiB     10.4 MiB   @profile
    10                             def arc():
    11                             
    12     10.4 MiB      0.0 MiB       tag = input("Введите знак (+,-,*,/, или 0 для выхода): ")
    13                             
    14     10.4 MiB      0.0 MiB       if tag == '0':
    15     10.4 MiB      0.0 MiB           print('выход')
    16                                 else:
    17     10.4 MiB      0.0 MiB           if tag in {'+', '-', '*', '/'}:
    18     10.4 MiB      0.0 MiB               x = float(input("x = "))
    19     10.4 MiB      0.0 MiB               y = float(input("y = "))
    20     10.4 MiB      0.0 MiB               if tag == '+':
    21     10.4 MiB      0.0 MiB                   print(f'{x + y:.2f}')
    22                                         elif tag == '-':
    23                                             print(f'{x - y:.2f}')
    24                                         elif tag == '*':
    25                                             print(f'{x * y:.2f}')
    26                                         elif y != 0:
    27                                             print(f'{x / y:.2f}')
    28                                         else:
    29                                             print("Делить на ноль нельзя!")
    30     10.4 MiB      0.0 MiB               return arc()  # ретерн вынесен за if
    31                                     else:
    32                                         print("Знак операции введен неверно!")
    33                                         return arc()

2 вариант
Line #    Mem usage    Increment   Line Contents
================================================
    39     10.4 MiB     10.4 MiB   @profile
    40                             def func():
    41                                 while True:
    42     10.4 MiB      0.0 MiB           tag = input("Введите знак (+,-,*,/, или 0 для выхода): ")
    43     10.4 MiB      0.0 MiB           if tag == '0':
    44     10.4 MiB      0.0 MiB               break
    45                                     else:
    46     10.4 MiB      0.0 MiB               if tag in {'+', '-', '*', '/'}:
    47     10.4 MiB      0.0 MiB                   x = float(input("x = "))
    48     10.4 MiB      0.0 MiB                   y = float(input("y = "))
    49     10.4 MiB      0.0 MiB                   if tag == '+':
    50     10.4 MiB      0.0 MiB                       print(f'{x + y:.2f}')
    51                                             elif tag == '-':
    52                                                 print(f'{x - y:.2f}')
    53                                             elif tag == '*':
    54                                                 print(f'{x * y:.2f}')
    55                                             elif y != 0:
    56                                                 print(f'{x / y:.2f}')
    57                                             else:
    58                                                 print("Делить на ноль нельзя!")
    59                                         else:
    60                                             print("Знак операции введен неверно!")

"""