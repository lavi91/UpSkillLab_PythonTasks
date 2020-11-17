"""Имеется набор файлов, каждый из которых, кроме последнего, содержит имя следующего файла.
Первое слово в тексте последнего файла: "We".

Скачайте предложенный файл. В нём содержится ссылка на первый файл из этого набора.

Все файлы располагаются в каталоге по адресу:
https://stepic.org/media/attachments/course67/3.6.3/

Загрузите содержимое последнего файла из набора, как ответ на это задание."""

import requests

with open('C:/Users/Vital/Documents/dataset_3378_3.txt') as inf:
    url = inf.readline().strip()
r = requests.get(url)
res = r.text
while res[0] + res[1] != 'We':
    new_url = 'https://stepic.org/media/attachments/course67/3.6.3/' + abc
    print(new_url)
    r = requests.get(new_url)
    res = r.text
print(res)
