def merged(left, right, result):
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    if i != len(left):
        for num in range(i, len(left)):
            result.append(left[num])
    if j != len(right):
        for num in range(j, len(right)):
            result.append(right[num])
    return result

def k_merge(*args):
    """
    Given an arbitrary number of sorted lists, build a merged sorted list.
    >>> k_merge()
    >>> k_merge([])
    []
    >>> k_merge([1], [1])
    [1, 1]
    >>> k_merge([1, 3], [5], [2, 4])
    [1, 2, 3, 4, 5]
    >>> k_merge([1, 1, 1], [3], [2, 2])
    [1, 1, 1, 2, 2, 3]
    >>> k_merge([1,4,5], [1,3,4], [2,6])
    [1, 1, 2, 3, 4, 4, 5, 6]
    """
    if not args:
        return
    result = []
    left = [i for i in args[0]]
    for i in range(1, len(args)):
        right = [j for j in args[i]]
        left = merged(left, right, result)
        result = []
    return left

































import heapq

def k_merge(*args):
    """
    Given an arbitrary number of sorted lists, build a merged sorted list.
    >>> k_merge()
    >>> k_merge([])
    []
    >>> k_merge([1], [1])
    [1, 1]
    >>> k_merge([1, 3], [5], [2, 4])
    [1, 2, 3, 4, 5]
    >>> k_merge([1, 1, 1], [3], [2, 2])
    [1, 1, 1, 2, 2, 3]
    >>> k_merge([1,4,5], [1,3,4], [2,6])
    [1, 1, 2, 3, 4, 4, 5, 6]
    """
    if not args:
        return
    return list(heapq.merge(*args))







import heapq

def k_merge(*args):
    """
    Given an arbitrary number of sorted lists, build a merged sorted list.
    >>> k_merge()
    >>> k_merge([])
    []
    >>> k_merge([1], [1])
    [1, 1]
    >>> k_merge([1, 3], [5], [2, 4])
    [1, 2, 3, 4, 5]
    >>> k_merge([1, 1, 1], [3], [2, 2])
    [1, 1, 1, 2, 2, 3]
    >>> k_merge([1,4,5], [1,3,4], [2,6])
    [1, 1, 2, 3, 4, 4, 5, 6]
    """
    if not args:
        return
    result = []
    for i in args:
        for j in i:
            result.append(j)
    heapq.heapify(result)
    return [heapq.heappop(result) for _ in range(len(result))]
