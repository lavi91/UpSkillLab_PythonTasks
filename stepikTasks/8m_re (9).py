"""Вам дана последовательность строк.
В каждой строке замените все вхождения нескольких одинаковых букв на одну букву.
Буквой считается символ из группы \w."""

import re

pattern = r"(\w)\1+"

import sys

for line in sys.stdin:
    line = line.rstrip()
    print(re.sub(pattern, r"\1", line))
