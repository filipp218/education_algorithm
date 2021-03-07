"""
Даны две таблицы T1 и T2. Каждая таблица представлена двумя числовыми полями. Таблица T1 содержит поля a и b. Таблица T2 содержит поля a и с.

Необходимо реализовать упрощенную вариацию SQL JOIN двух таблиц по полю a и сформировать таблицу T3.

Значения поля a в таблице могут дублироваться, но количество дублирований каждого поля не превышает 5. Ограничение времени: 1 с, ограничение памяти: 64 МБ.
"""

def inner_join(t1, t2):
    """
    >>> inner_join([(1, 2), (2, 2)], [(1, 3), (2, 4)])
    [(1, 2, 3), (2, 2, 4)]
    >>> inner_join([(1, 2), (1, 3), (2, 5)], [(1, 1), (2, 0)])
    [(1, 2, 1), (1, 3, 1), (2, 5, 0)]
    """
    b_by_a = {}
    for a, b in t1:
        if a not in b_by_a:
            b_by_a[a] = []
        b_by_a[a].append(b)

    result = []
    for a, c in t2:
        if a in b_by_a:
            for b in b_by_a[a]:
                item = (a, b, c)
                result.append(item)
    return result


def left_join(t1, t2):
    """
    >>> left_join([(1, 2), (1, 3), (0, 1)], [(1, 10), (1, 20), (2, 40)])
    [(1, 2, 10), (1, 2, 20), (1, 3, 10), (1, 3, 20), (0, 1, None)]
    """
    с_by_a = {}
    for a, с in t2:
        if a not in с_by_a:
            с_by_a[a] = []
        с_by_a[a].append(с)

    result = []
    for a, b in t1:
        if a in с_by_a:
            for c in с_by_a[a]:
                item = (a, b, c)
                result.append(item)
        else:
            item = (a, b, None)
            result.append(item)

    return result

def right_join(t1, t2):
    """
    >>> right_join([(1, 2), (1, 3), (0, 1)], [(1, 10), (1, 20), (2, 40)])
    [(1, 2, 10), (1, 3, 10), (1, 2, 20), (1, 3, 20), (2, None, 40)]
    """
    b_by_a = {}
    for a, b in t1:
        if a not in b_by_a:
            b_by_a[a] = []
        b_by_a[a].append(b)

    result = []
    for a, c in t2:
        if a in b_by_a:
            for b in b_by_a[a]:
                item = (a, b, c)
                result.append(item)
        else:
            item = (a, None, c)
            result.append(item)
    return result

def full_join(t1, t2):
    """
    >>> full_join([(1, 2), (1, 3), (0, 1)], [(1, 10), (1, 20), (2, 40)])
    [(1, 2, 10), (1, 2, 20), (1, 3, 10), (1, 3, 20), (0, 1, None), (2, None, 40)]
    """
    с_by_a = {}
    for a, с in t2:
        if a not in с_by_a:
            с_by_a[a] = []
        с_by_a[a].append(с)

    b_by_a = {}
    for a, b in t1:
        if a not in b_by_a:
            b_by_a[a] = []
        b_by_a[a].append(b)

    result = []
    for a, b in t1:
        if a in с_by_a:
            for c in с_by_a[a]:
                item = (a, b, c)
                result.append(item)
        else:
            item = (a, b, None)
            result.append(item)

    for a, c in t2:
        if a not in b_by_a:
            item = (a, None, c)
            result.append(item)

    return result

n1 = int(input())
t1 = []
t2 = []
for i in range(n1):
    a, b = int(input().split())
    item = (a, b)
    t1.append(item)

n2 = int(input())
for i in range(n2):
    a, c = int(input().split())
    item = (a, c)
    t2.append(item)

connect = input()
if connect == 'INNER':
    print(inner_join(t1, t2))
elif connect == 'LEFT':
    print(left_join(t1, t2))
elif connect == 'RIGHT':
    print(right_join(t1, t2))
elif connect == 'FULL':
    print(full_join(t1, t2))
