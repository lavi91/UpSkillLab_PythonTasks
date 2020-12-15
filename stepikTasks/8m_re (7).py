"""Вам дана последовательность строк.
В каждой строке замените первое вхождение слова, состоящего только из латинских букв "a" (регистр не важен),
на слово "argh".

Примечание:
Обратите внимание на параметр count у функции sub."""

import re

pattern = r"\ba+\b"

import sys

for line in sys.stdin:
    line = line.rstrip()
    if re.search(pattern, line, re.IGNORECASE):
        res = re.sub(pattern, "argh", line, 1, re.IGNORECASE)
        print(res)
    else:
        print(line)
