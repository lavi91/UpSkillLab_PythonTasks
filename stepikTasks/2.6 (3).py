"""Напишите программу, которая считывает список чисел lstlst из первой строки и число xx из второй строки,
которая выводит все позиции, на которых встречается число xx в переданном списке lstlst.

Позиции нумеруются с нуля, если число xx не встречается в списке, вывести строку "Отсутствует" (без кавычек,
                                                                                                    с большой буквы).

Позиции должны быть выведены в одну строку, по возрастанию абсолютного значения."""

lst = [int(i) for i in input().split()]
x = int(input())
result = []
i = 0
while i < len(lst):
    if lst[i] == x:
        result += [i]
    i += 1
if len(result) == 0:
    print('Отсутствует')
else:
    print(*result)