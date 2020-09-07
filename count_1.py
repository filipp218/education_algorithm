
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
    import heapq  
    
    result = numbers[:k]
    heapq.heapify(result)
    mins = result[0]

    for value in numbers[k:]:
        if value > mins:
            heapq.heappop(result)
            heapq.heappush(result, value)
            mins = result[0]
    return mins
    
    
    
    
    
    
    
    
    import heapq   #O(n)
    result = []
    for value in numbers:
        heapq.heappush(result, value)
    result = [ heapq.heappop(result) for _ in range(len(result))]
    return result[-k]



    buffer = numbers[:k]
    for n in numbers[k:]:  # O(n)
        mins = buffer[0]  # O(1)
        if n > mins:
            buffer.pop(0)  # O(log(k))
            buffer.append(n)  # O(log(k))
    return min(buffer)  # O(n * log(k))


    for i in range(k-1):
        maxs = max(numbers)
        numbers.remove(maxs)
    return max(numbers)  # O(n * k)


    result = sorted(numbers)  # O(n * log(n))
    return result[-k]  # O(1)
