"""
Задание 2.
Ваша программа должна запрашивать пароль
Для этого пароля вам нужно получить хеш, используя функцию sha256
Для генерации хеша обязательно нужно использовать криптографическую соль
Обязательно выведите созданный хеш

Далее программа должна запросить пароль повторно
Вам нужно проверить, совпадает ли пароль с исходным
Для проверки необходимо сравнить хеши паролей

ПРИМЕР:
Введите пароль: 123
В базе данных хранится строка: 555a3581d37993843efd4eba1921f1dcaeeafeb855965535d77c55782349444b
Введите пароль еще раз для проверки: 123
Вы ввели правильный пароль
"""

from uuid import uuid4
import hashlib

salt = uuid4().hex
print(f'соль: {salt}')


def take_hash(passwd_obj):
    return hashlib.sha256(salt.encode() + passwd_obj.encode()).hexdigest() + ':' + salt


def hash_tick(hash_password, user_password):
    return hash_password == hashlib.sha256(salt.encode() + user_password.encode()).hexdigest() + ':' + salt


username = 'Blum'
user_obj = '456blum'

new_passwd_obj = input('введите пароль: ')
hash_obj = take_hash(user_obj)
print(f'пароль в базе данных: {hash_obj}')

old_passwd_obj = input('введите пароль еще раз для проверки: ')

if hash_tick(hash_obj, old_passwd_obj):
    print('Пароль правильный')
else:
    print('Пароль неверный')

"""
# доделать

from hashlib import pbkdf2_hmac
import hashlib

salt = b''  # соли, сохраненной для пользователя
key = b''  # рассчитан ключ пользователя

password_to_check = 'password456'  # Пароль, сохраненный пользователем, проверяется

# вставляется для проверки настоящий пароль
new_key = hashlib.pbkdf2_hmac('sha256',
                              password_to_check.encode(),
                              salt, 100000)
if new_key == key:
    print('Пароль правильный')
else:
    print('Пароль неправильный')
"""
