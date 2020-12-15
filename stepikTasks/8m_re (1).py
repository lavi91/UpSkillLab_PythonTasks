"""Вам дана последовательность строк.
Выведите строки, содержащие "cat" в качестве подстроки хотя бы два раза.

Примечание:
Считать все строки по одной из стандартного потока ввода вы можете, например, так

import sys

for line in sys.stdin:
    line = line.rstrip()
    # process line"""

import re

pattern = r"cat"

import sys

for line in sys.stdin:
    line = line.rstrip()
    res = re.findall(pattern, line)
    if len(res) > 1:
        print(line)
    else:
        continue
