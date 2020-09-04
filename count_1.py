
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
    >>> kth_largest([-10, -9, 5, -6, 4, 7, 2, 1, 3, 8], 3)
    8
    >>> kth_largest([10, 10, 15, 6, 6, 6, 2, 7, 7, 8], 3)
    7
    >>> kth_largest([-10, 9, -5, 6, 4, 7, -2, 1, 3, -8], 3)
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

    result = []
    for i in range (0, minus_lines):
        result.extend([i + bottom_line] * diapazon[i])

    place = 0
    last = result[-1]
    how_digit = 1
    for elem in reversed(result):
        if elem != last:
            how_digit += 1
            last = elem
        if how_digit > k:
            break
        place += 1

    return len(result) - (place - 1)
