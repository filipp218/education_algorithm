def counter(k):
    """
    >>> counter([1, 2, 3, 4, 5, 5, 5, 6, 6, 6, 7, 7, 8, 9, 9, 9])
    9
    """
    numbs = {}
    for i in k:
        if i in numbs:
            numbs[i] += 1
        else:
            numbs[i] = 1
    max = numbs[k[0]]
    digit = k[0]
    for i in numbs:
        if numbs[i]>=max:
            max = numbs[i]
            digit = i
    return digit