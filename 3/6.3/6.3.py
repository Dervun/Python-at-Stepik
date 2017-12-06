"""
Имеется набор файлов, каждый из которых, кроме последнего, содержит имя следующего файла.
Первое слово в тексте последнего файла: "We".

Скачайте предложенный файл. В нём содержится ссылка на первый файл из этого набора.

Все файлы располагаются в каталоге по адресу:
http://stepic.org/media/attachments/course67/3.6.3/

Загрузите содержимое ﻿последнего файла из набора, как ответ на это задание.
"""

from requests import get

r = get('http://stepic.org/media/attachments/course67/3.6.3/699991.txt')
while r.text < 'We' or r.text >= 'Wf':
    print(r.text)
    r = get(url='http://stepic.org/media/attachments/course67/3.6.3/' + r.text.strip())
print(r.text)

