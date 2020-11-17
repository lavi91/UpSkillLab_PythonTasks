"""Напишите программу, которая считывает строку с числом n, которое задаёт количество чисел, которые нужно считать.
Далее считывает n строк с числами x, по одному числу в каждой строке. Итого будет n+1 строк.

При считывании числа x программа должна на отдельной строке вывести значение f(x). Функция f(x) уже реализована и
доступна для вызова.

Функция вычисляется достаточно долго и зависит только от переданного аргумента x. Для того, чтобы уложиться
в ограничение по времени, нужно избежать повторного вычисления значений."""

n = int(input())
lst = []
s = {}
i = 0
while i < n:
    x = int(input())
    if x not in s:
        s[x] = f(x)         # функция уже описана в Stepik. Суть задания, как я понял, сократить количество ее вызовов
        lst.append(s[x])
    else:
        lst.append(s[x])
    i += 1
for i in lst:
    print(i)