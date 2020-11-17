"""На прошлой неделе мы сжимали строки, используя кодирование повторов. Теперь нашей задачей будет восстановление
исходной строки обратно.

Напишите программу, которая считывает из файла строку, соответствующую тексту, сжатому с помощью кодирования
повторов, и производит обратную операцию, получая исходный текст.

Запишите полученный текст в файл и прикрепите его, как ответ на это задание.

В исходном тексте не встречаются цифры, так что код однозначно интерпретируем.

Примечание. Это первое задание типа Dataset Quiz. В таких заданиях после нажатия "Start Quiz" у вас появляется
ссылка "download your dataset". Используйте эту ссылку для того, чтобы загрузить файл со входными данными к себе
на компьютер. Запустите вашу программу, используя этот файл в качестве входных данных. Выходной файл, который при
этом у вас получится, надо отправить в качестве ответа на эту задачу."""


"""
считываем условия задания для программы:
inf = open('C:/Users/Vital/Documents/dataset_3363_2.txt', 'r')
s = inf.readline().strip()
inf.close()"""

n = s
s = set() # создаем множество из строк, состоящих из чисел
for i in range(0, 10):
    s.add(str(i))
f = '' # здесь записываем число, показывающее количство конкретной буквы. Если число многозначное, то будем склеивать его составляющие
letter = [] # в этом списке будем хранить буквы
factor = [] # в этом списке будем хранить числа.
i = 0
while i < len(n):
    if i + 1 == len(n):
        f += n[i]
        factor += [f]
        f = ''
    elif n[i] in s and n[i + 1] in s:
        f += n[i]
    elif n[i] in s:
        f += n[i]
        factor += [f]
        f = ''
    else:
        letter += [n[i]]
    i += 1

result = ''
j = 0
while j < len(letter):
    result += letter[j] * int(factor[j])
    j += 1


"""
запись резульатат работы программы в файл
ouf = open('C:/Users/Vital/Documents/result.txt', 'w')
ouf.write(result)
ouf.close()"""


