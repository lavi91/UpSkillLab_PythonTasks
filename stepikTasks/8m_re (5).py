"""Вам дана последовательность строк.
Выведите строки, содержащие слово, состоящее из двух одинаковых частей (тандемный повтор).

Sample Input:

blabla is a tandem repetition
123123 is good too
go go
aaa

Sample Output:

blabla is a tandem repetition
123123 is good too"""

import re

pattern = r"\b(\w+)\1\b"

import sys

for line in sys.stdin:
    line = line.rstrip()
    res = re.findall(pattern, line)
    if len(res) > 0:
        print(line)
    else:
        continue
