"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования
Можете условжнить задачу, реализовав ее через ООП
"""

from uuid import uuid4
import hashlib

salt = uuid4().hex
cache_obj = {}


def take_page(url):
    if cache_obj.get(url):
        return url
    else:
        url_slt = hashlib.sha256(salt.encode() + url.encode()).hexdigest() + ':' + salt
        cache_obj[url] = url_slt
        print(cache_obj)
    print(f'Данный адрес: {url} присутствует в кэше')  # print выносим за if чтобы не повторяться в коде


take_page('https://developers.google.com/')
