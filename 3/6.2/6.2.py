"""Посчитать число строк в файле"""
from requests import get

r = get('https://stepic.org/media/attachments/course67/3.6.2/429.txt')
print('\n'.join(r.text.splitlines()))
print(len(r.text.splitlines()))
