"""Вашей программе на вход подаются две строки s и t, состоящие из строчных латинских букв.

Выведите одно число – количество вхождений строки t в строку s.

Пример:
s = "abababa"
t = "aba"

Вхождения строки t в строку s:
ABAbaba
abABAba
ababABA"""

s = input()
t = input()
cnt = 0
i = 0
while i < len(s):
    if s[i:].startswith(t):
        cnt += 1
        i += 1
    else:
        i += 1
print(cnt)
