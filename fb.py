def how(a,b):
    """
    >>> how("11", "123")
    '134'

    >>> how("99", "11")
    '110'

    >>> how("0", "123")
    '123'
    """
    numbers = {'0':0, '1':1,'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}
    over = 0
    result = []

    if len(a)==1 and len(b)==1:
        sum = numbers[a[0]] + numbers[b[0]]
        return str(sum)

    elif len(a) == 0:
        return b

    elif len(b) == 0:
        return a

    if len(b) > len(a):
        a,b = b,a
    i = -1
    while i*(-1) != len(b)+1:
        sum = numbers[a[i]] + numbers[b[i]]
        sum += over
        over = 0
        if sum > 9:
            over = 1
            result.append(str(sum - 10))
        else:
            result.append(str(sum))
        i -=1
    if over > 0 and len(a) > len(b):
        sum = numbers[a[i]] + over
        over = 0
        result.append(str(sum))

    elif over > 0:
        result.append(str(1))


    while i*(-1) != len(a)+1:
        result.append(str(numbers[a[i]]))
        i -= 1

    result.reverse()
    return (''.join(result))
