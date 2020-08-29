def counter_sort(numbers):
    """
    >>> counter_sort([2, 1, 4, 3, 6, 5])
    [1, 2, 3, 4, 5, 6]
    >>> counter_sort([10, 15, 13, 12, 11, 14])
    [10, 11, 12, 13, 14, 15]
    >>> counter_sort([0, -10, 1, 2, 3, -5])
    [-10, -5, 0, 1, 2, 3]
    >>> counter_sort([])
    []
    """
    if not numbers:
        return numbers

    diapazon= [0] * 2000  
    for num in numbers:
        if num >=0:  #если число положительное добавляем его список с положительными
            diapazon[num] += 1
            continue
        diapazon[num] += 1  #если число отрицательное добавляем его список с отрицательными

    result = []  
    for i in range(1000,2000):  
        result.extend([i - 2000 for j in range(diapazon[i])])
    for i in range (0, 1000):
        result.extend([i for j in range(diapazon[i])])
    return result