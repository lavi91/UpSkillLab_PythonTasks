"""Напишите программу, на вход которой подаётся прямоугольная матрица в виде последовательности строк,
заканчивающихся строкой, содержащей только строку "end" (без кавычек)

Программа должна вывести матрицу того же размера, у которой каждый элемент в позиции i, j равен сумме
элементов первой матрицы на позициях (i-1, j), (i+1, j), (i, j-1), (i, j+1). У крайних символов соседний
элемент находится с противоположной стороны матрицы.

В случае одной строки/столбца элемент сам себе является соседом по соответствующему направлению."""

st = input().split()
row = 0
column = len(st)
a = []
while st != ['end']:
    i = 0
    while i < len(st):
        st[i] = int(st[i]) # IDE выделяет i в st[i]. Криво реализовано? Я пробовал другие варианты, но не получалось.
        i += 1
    a.append(st)
    row += 1
    st = input().split()
result = [[0 for j in range(column)] for i in range(row)]
for i in range(row):
    for j in range(column):
        if j + 1 == column and i + 1 == row:
            result[i][j] = a[i - 1][j] + a[i + 1 - row][j] + a[i][j - 1] + a[i][j + 1 - column]
        elif i + 1 == row:
            result[i][j] = a[i - 1][j] + a[i + 1 - row][j] + a[i][j - 1] + a[i][j + 1]
        elif j + 1 == column:
            result[i][j] = a[i - 1][j] + a[i + 1][j] + a[i][j - 1] + a[i][j + 1 - column]
        else:
            result[i][j] = a[i - 1][j] + a[i + 1][j] + a[i][j - 1] + a[i][j + 1]
for i in result:
    print(*i)