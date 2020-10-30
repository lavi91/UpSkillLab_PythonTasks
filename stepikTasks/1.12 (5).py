"""Напишите программу, которая получает на вход три целых числа, по одному числу в строке, и выводит на консоль
в три строки сначала максимальное, потом минимальное, после чего оставшееся число.

На ввод могут подаваться и повторяющиеся числа."""

a = int(input())
b = int(input())
c = int(input())
max = a
min = b
num = c
if (b >= max):
    max = b
if (c >= max):
    num = max
    max = c
if (a <= min):
    min = a
if (c <= min):
    num = min
    min = c
print(max)
print(min)
print(num)