"""Вам дана последовательность строк.
Выведите строки, содержащие обратный слеш "\"."""

import re

pattern = r"\\"

import sys

for line in sys.stdin:
    line = line.rstrip()
    res = re.findall(pattern, line)
    if len(res) > 0:
        print(line)
    else:
        continue
