"""Вам дана последовательность строк.
Выведите строки, содержащие две буквы "z", между которыми ровно три символа.
"""
import re

pattern = r"z\w{3}z"

import sys

for line in sys.stdin:
    line = line.rstrip()
    res = re.findall(pattern, line)
    if len(res) > 0:
        print(line)
    else:
        continue
