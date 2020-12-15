"""Вам дана последовательность строк.
В каждой строке замените все вхождения подстроки "human" на подстроку "computer" и выведите полученные строки."""

import re

pattern = r"human"

import sys

for line in sys.stdin:
    line = line.rstrip()
    if re.search(pattern, line):
        res = re.sub(pattern, "computer", line)
        print(res)
    else:
        print(line)
