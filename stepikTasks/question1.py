"""Вам дано описание наследования классов в следующем формате.
<имя класса 1> : <имя класса 2> <имя класса 3> ... <имя класса k>
Это означает, что класс 1 отнаследован от класса 2, класса 3, и т. д.

Или эквивалентно записи:
class Class1(Class2, Class3 ... ClassK):
    pass

Класс A является прямым предком класса B, если B отнаследован от A:
class B(A):
    pass

Класс A является предком класса B, если
A = B;
A - прямой предок B
существует такой класс C, что C - прямой предок B и A - предок C

Например:
class B(A):
    pass

class C(B):
    pass

# A -- предок С

Вам необходимо отвечать на запросы, является ли один класс предком другого класса

Важное примечание:
Создавать классы не требуется.
Мы просим вас промоделировать этот процесс, и понять существует ли путь от одного класса до другого.

Формат входных данных
В первой строке входных данных содержится целое число n - число классов.

В следующих n строках содержится описание наследования классов. В i-й строке указано от каких классов
наследуется i-й класс. Обратите внимание, что класс может ни от кого не наследоваться. Гарантируется, что класс
не наследуется сам от себя (прямо или косвенно), что класс не наследуется явно от одного класса более одного раза.

В следующей строке содержится число q - количество запросов.

В следующих q строках содержится описание запросов в формате <имя класса 1> <имя класса 2>.
Имя класса – строка, состоящая из символов латинского алфавита, длины не более 50.

Формат выходных данных
Для каждого запроса выведите в отдельной строке слово "Yes", если класс 1 является предком класса 2, и "No",
если не является.
"""



all_classes = {}
n1 = int(input())
for i in range(n1):
    a, *b = input().replace(':', ' ').split()
    all_classes[a] = b

parents = []


def check_parent(parent, child):
    global parents
    if child not in all_classes:
        all_classes[child] = []
    parents += all_classes[child]
    for elem in all_classes[child]:
        check_parent(parent, elem)


n2 = int(input())
for i in range(n2):
    c, d = input().split()
    if c == d:
        print('Yes')
    elif c in all_classes[d]:
        print('Yes')
    elif c == d:
        print('Yes')
    else:
        check_parent(c, d)
        if c in parents:
            print('Yes')
        else:
            print('No')
print(all_classes)
print(parents)
