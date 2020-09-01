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
    >>> counter_sort([10, 11, 10])
    [10, 10, 11]
    """
    if not numbers:
        return numbers

    upper_line = max(numbers) + 1  #прибавляем единицу, потому что список с нуля начинает считать
    bottom_line = min(numbers)

    minus_lines = upper_line - bottom_line
    diapazon = [0] * minus_lines

    for num in numbers:
        diapazon[num - bottom_line] += 1
    result = []
    for i in range (0, minus_lines):
        result.extend([i + bottom_line] * diapazon[i])

    return result
