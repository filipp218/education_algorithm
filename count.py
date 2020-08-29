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

    diapazon_plus = [0] * 1000  #положительные
    diapazon_minus = [0] * 1000  #отрицательные
    for num in numbers:
        if num >=0:  #если число положительное добавляем его список с положительными
            diapazon_plus[num] += 1
            continue
        diapazon_minus[-num] += 1  #если число отрицательное добавляем его список с отрицательными

    result = []  #создаём список, куда сначала добавим отрицателнье
    for i in range(len(diapazon_minus)- 1, 0 , -1):  #цикл делаем с конца диапазона
        if diapazon_minus[i] > 0:  #если на месте индекса не ноль, значит это число было изначально
            for num in range(diapazon_minus[i]):  #добавляем это число столько раз,сколько оно встретилось
                result.append(-i)

    for i in range(len(diapazon_plus)):
        if diapazon_plus[i] > 0:
            for num in range(diapazon_plus[i]):
                result.append(i)
    return result
