"""Напишите программу, которая выводит часть последовательности 1 2 2 3 3 3 4 4 4 4 5 5 5 5 5 ...
(число повторяется столько раз, чему равно). На вход программе передаётся неотрицательное целое
число n — столько элементов последовательности должна отобразить программа. На выходе ожидается
последовательность чисел, записанных через пробел в одну строку.

Например, если n = 7, то программа должна вывести 1 2 2 3 3 3 4."""

a = int(input())
lt = []
i = 1
while i <= a:
    lt += [i] * i
    i += 1
j = 0
while j < a:
    print(lt[j], end=' ')
    j += 1