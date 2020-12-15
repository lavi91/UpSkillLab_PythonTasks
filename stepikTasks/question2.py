"""n = int(input())
d_err = {}
for i in range(n):
    a, *b = input().replace(':', ' ').split()
    d_err[a] = b"""

d_err = {'BaseException': [],
         'Exception': ['BaseException'],
         'LookupError': ['Exception '],
         'KeyError': ['LookupError']}

a = ['BaseException',
     'KeyError']

catch_err = set()


def f(parent):
    global d_err, catch_err
    if parent in catch_err:
        print(parent)
    catch_err.add(parent)
    for child in d_err[parent]:
        if child in d_err:
            f(child)


for elem in a:
    if elem in catch_err:
        print(elem)
    else:
        if len(d_err[elem]) == 0:
            catch_err.add(elem)
        elif elem not in d_err:
            catch_err.add(elem)
        else:
            catch_err.add(elem)
            for x in d_err[elem]:
                if x in catch_err:
                    print(elem)
                    break
                elif x in d_err:
                    f(x)

