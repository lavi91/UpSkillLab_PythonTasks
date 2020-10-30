"""Узнав, что ДНК не является случайной строкой, только что поступившие в Институт биоинформатики студенты группы
информатиков предложили использовать алгоритм сжатия, который сжимает повторяющиеся символы в строке.

Кодирование осуществляется следующим образом:
s = 'aaaabbсaa' преобразуется в 'a4b2с1a2', то есть группы одинаковых символов исходной строки заменяются на этот
символ и количество его повторений в этой позиции строки.

Напишите программу, которая считывает строку, кодирует её предложенным алгоритмом и выводит закодированную
последовательность на стандартный вывод. Кодирование должно учитывать регистр символов."""

s = input()
cnt = 1
for i in range(0, len(s)):
    if i + 1 > len(s)-1:
        print(s[i] + str(cnt))
        break
    if s[i] == s[i + 1]:
        cnt += 1
    else:
        print(s[i] + str(cnt), end='')
        cnt = 1