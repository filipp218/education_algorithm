def kth_largest(numbers, k):
    """
    See https://leetcode.com/problems/kth-largest-element-in-an-array/
    >>> kth_largest([3, 2, 1, 5, 6, 4], 2)
    5
    >>> kth_largest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4)
    4
    >>> kth_largest([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 2)
    9
    >>> kth_largest([10, 9, 5, 6, 4, 7, 2, 1, 3, 8], 3)
    8
    """
    if not numbers:
        return numbers

    upper_line = max(numbers) + 1  #прибавляем единицу, потому что список с нуля начинает считать
    bottom_line = min(numbers)

    minus_lines = upper_line - bottom_line
    diapazon = [0] * minus_lines

    for num in numbers:
        diapazon[num - bottom_line] += 1

    element = len(diapazon) - (k-1)  # Узнаём под каким индексом наш эелемент
    place = 1  #счётчик, чтобы посчитать сколько цифр перед нашим элементом, единица чтобы прибавить наш первый элемент
    for i in range (0, element -1):
        place += diapazon[i]

    return place

