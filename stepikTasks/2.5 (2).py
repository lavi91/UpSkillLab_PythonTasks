"""Напишите программу, на вход которой подаётся список чисел одной строкой. Программа должна для каждого элемента
этого списка вывести сумму двух его соседей. Для элементов списка, являющихся крайними, одним из соседей считается
элемент, находящий на противоположном конце этого списка. Например, если на вход подаётся список "1 3 5 6 10", то
на выход ожидается список "13 6 9 15 7" (без кавычек).

Если на вход пришло только одно число, надо вывести его же.

Вывод должен содержать одну строку с числами нового списка, разделёнными пробелом."""

st = [int(i) for i in input().split()]
result = [0] * len(st)
i = 0
if len(st) == 1:
    print(st[0])
else:
    while i < len(st):
        if (i - 1) < 0:
            result[i] = st[len(st) - 1] + st[i + 1]
        elif i + 1 > len(st) - 1:
            result[i] = st[i - 1] + st[0]
        else:
            result[i] = st[i - 1] + st[i + 1]
        print(result[i], end=' ')
        i += 1