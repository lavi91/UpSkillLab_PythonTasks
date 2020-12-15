"""Вам дана последовательность строк.
Выведите строки, содержащие "cat" в качестве слова."""

import re

pattern = r"\bcat\b"

import sys

for line in sys.stdin:
    line = line.rstrip()
    res = re.findall(pattern, line)
    if len(res) > 0:
        print(line)
    else:
        continue
