
import string


def printer(seq):
    """
    >>> printer('azm')
    14
    >>> printer('bza')
    4
    """
    alpha_time = {}  #const
    llen = len(string.ascii_lowercase)
    for char in string.ascii_lowercase:  #const
        alpha_time[char] = ord(char) - ord('a')
    result = 0
    start = 0
    for char in seq:  #O(n)
        if start > alpha_time[char]:
            next = llen - start + alpha_time[char]
            prev = start - alpha_time[char]
        else:
            next = alpha_time[char] - start
            prev = llen - alpha_time[char] + start
        result += min(next, prev)
        start = alpha_time[char]

    return result



def printer(seq):
    """
    >>> printer('azm')
    14
    >>> printer('bza')
    4
    """
    alpha_time = {}  #const
    count_time = {}
    llen = len(string.ascii_lowercase)
    for char in string.ascii_lowercase:  #const
        alpha_time[char] = ord(char) - ord('a')

    for char in string.ascii_lowercase:
        start = alpha_time[char]
        if not char in count_time:
            count_time[char] = {}
        for elem in string.ascii_lowercase:#O(n)
            if elem not in count_time[char]:
                if start > alpha_time[elem]:
                    next = llen - start + alpha_time[elem]
                    prev = start - alpha_time[elem]
                else:
                    next = alpha_time[elem] - start
                    prev = llen - alpha_time[elem] + start
                di = count_time[char]
                di[elem] = min(next, prev)
                if elem not in count_time:
                    count_time[elem] = {}
                di = count_time[elem]
                di[char] = min(next, prev)


    result = 0
    start = 'a'
    for char in seq:
        result += count_time[start][char]
        start = char
    return result

import string


def printer(seq):
    """
    >>> printer('azm')
    14
    >>> printer('bza')
    4
    """
    alpha_time = {}  #const
    llen = len(string.ascii_lowercase)
    for char in string.ascii_lowercase:  #const
        alpha_time[char] = ord(char) - ord('a')
    result = 0
    start = 0
    for char in seq:  #O(n)
        if start > alpha_time[char]:
            next = llen - start + alpha_time[char]
            prev = start - alpha_time[char]
        else:
            next = alpha_time[char] - start
            prev = llen - alpha_time[char] + start
        result += min(next, prev)
        start = alpha_time[char]

    return result



def printer(seq):
    """
    >>> printer('azm')
    14
    >>> printer('bza')
    4
    """
    alpha_time = {}  #const
    count_time = {}
    llen = len(string.ascii_lowercase)
    for char in string.ascii_lowercase:  #const
        alpha_time[char] = ord(char) - ord('a')

    for char in string.ascii_lowercase:
        start = alpha_time[char]
        if not char in count_time:
            count_time[char] = {}
        for elem in string.ascii_lowercase:#O(n)
            if elem not in count_time[char]:
                if start > alpha_time[elem]:
                    next = llen - start + alpha_time[elem]
                    prev = start - alpha_time[elem]
                else:
                    next = alpha_time[elem] - start
                    prev = llen - alpha_time[elem] + start
                di = count_time[char]
                di[elem] = min(next, prev)
                if elem not in count_time:
                    count_time[elem] = {}
                di = count_time[elem]
                di[char] = min(next, prev)


    result = 0
    start = 'a'
    for char in seq:
        result += count_time[start][char]
        start = char
    return result


import string


def printer(seq):
    """
    >>> printer('azm')
    14
    >>> printer('bza')
    4
    """
    alpha_time = {}  #const
    llen = len(string.ascii_lowercase)
    for char in string.ascii_lowercase:  #const
        alpha_time[char] = ord(char) - ord('a')
    result = 0
    start = 0
    for char in seq:  #O(n)
        if start > alpha_time[char]:
            next = llen - start + alpha_time[char]
            prev = start - alpha_time[char]
        else:
            next = alpha_time[char] - start
            prev = llen - alpha_time[char] + start
        result += min(next, prev)
        start = alpha_time[char]

    return result



def printer(seq):
    """
    >>> printer('azm')
    14
    >>> printer('bza')
    4
    """
    alpha_time = {}  #const
    couimport string


def printer(seq):
    """
    >>> printer('azm')
    14
    >>> printer('bza')
    4
    """
    alpha_time = {}  #const
    llen = len(string.ascii_lowercase)
    for char in string.ascii_lowercase:  #const
        alpha_time[char] = ord(char) - ord('a')
    result = 0
    start = 0
    for char in seq:  #O(n)
        if start > alpha_time[char]:
            next = llen - start + alpha_time[char]
            prev = start - alpha_time[char]
        else:
            next = alpha_time[char] - start
            prev = llen - alpha_time[char] + start
        result += min(next, prev)
        start = alpha_time[char]

    return result



def printer(seq):
    """
    >>> printer('azm')
    14
    >>> printer('bza')
    4
    """
    alpha_time = {}  #const
    count_time = {}
    llen = len(string.ascii_lowercase)
    for char in string.ascii_lowercase:  #const
        alpha_time[char] = ord(char) - ord('a')

    for char in string.ascii_lowercase:
        start = alpha_time[char]
        if not char in count_time:
            count_time[char] = {}
        for elem in string.ascii_lowercase:#O(n)
            if elem not in count_time[char]:
                if start > alpha_time[elem]:
                    next = llen - start + alpha_time[elem]
                    prev = start - alpha_time[elem]
                else:
                    next = alpha_time[elem] - start
                    prev = llen - alpha_time[elem] + start
                di = count_time[char]
                di[elem] = min(next, prev)
                if elem not in count_time:
                    count_time[elem] = {}
                di = count_time[elem]
                di[char] = min(next, prev)


    result = 0
    start = 'a'
    for char in seq:
        result += count_time[start][char]
        start = char
    return result

nt_time = {}
    llen = len(string.ascii_lowercase)
    for char in string.ascii_lowercase:  #const
        alpha_time[char] = ord(char) - ord('a')

    for char in string.ascii_lowercase:
        start = alpha_time[char]
        if not char in count_time:
            count_time[char] = {}
        for elem in string.ascii_lowercase:#O(n)
            if elem not in count_time[char]:
                if start > alpha_time[elem]:
                    next = llen - start + alpha_time[elem]
                    prev = start - alpha_time[elem]
                else:
                    next = alpha_time[elem] - start
                    prev = llen - alpha_time[elem] + start
                di = count_time[char]
                di[elem] = min(next, prev)
                if elem not in count_time:
                    count_time[elem] = {}
                di = count_time[elem]
                di[char] = min(next, prev)


    result = 0
    start = 'a'
    for char in seq:
        result += count_time[start][char]
        start = char
    return result

