"""
3.	Сформировать из введенного числа обратное по порядку входящих в него
цифр и вывести на экран. Например, если введено число 3486,
 то надо вывести число 6843.

Подсказка:
На каждом шаге вам нужно 'доставать' из числа очередную цифру
Пока все числа не извлечены рекурсивные вызовы продолжаем
Условие завершения рекурсии - все числа извлечены

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7

Пример:
Введите число, которое требуется перевернуть: 123
Перевернутое число: 321
"""


def back(n, m=0):

    if n == 0:
        return m
    if n > 0:
        m = m * 10 + n % 10
        n = n // 10
        return back(n, m)


try:
    NUMB = int(input("Введите число: "))
    print(f"Перевернутое число: {back(NUMB)}")
except ValueError:
    print("введите число")


"""

# цикл

BASE = 10

num = int(input('Введите целое число: '))
result = 0
while num > 0:
    result = result * BASE + num % BASE
    num = num // BASE
print(result)


n = int(input())
m = 0
while n>0:
    m = m*10 + n%10
    n = n//10
print(m)

"""

