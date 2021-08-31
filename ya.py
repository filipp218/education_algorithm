Задача с собеседований в Яндекс
Дана последовательность из N -1 чисел. Известно что в ней в случайном порядке есть все числа от 1 до N
кроме одного числа. Нужно найти пропущенное число с минимальными расходами памяти


>> [1, 7, 8, 6, 5, 4, 2]
<< 3


def func(seq): #O(n)
    s = sum(i for i in range(len(seq) + 1))
    return s - sum(seq)


def func(seq): #(N log n) по времени
    seq.sort()
    previus = seq[0]
    for nexts in seq[1::]:
        if nexts - previus == 2:
            return previus + 1
        previus = nexts
