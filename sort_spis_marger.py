def merge_sorted_lens(A):
    if len(A) <= 1:
        return(A)
    else:
        middle = int(len(A) / 2)
        left_side = merge_sorted_lens(A[:middle])
        right_side = merge_sorted_lens(A[middle:])
        return merger(left_side, right_side)

def merger(left_side, right_side):
    result = []
    while len(left_side) > 0 and len(right_side) > 0:
        if len(left_side[0]) >= len(right_side[0]):
            result.append(left_side[0])
            left_side = left_side[1:]
        else:
            result.append(right_side[0])
            right_side = right_side[1:]
    if len(left_side) > 0:
        result += left_side
    if len(right_side) > 0:
        result += right_side
    return result

def sort_letters(text):
    """
    >>> sort_letters('aaabccccdeefffff')
    'fffffccccaaaeebd'
    >>> sort_letters('abcdefghijklmnop')
    'abcdefghijklmnop'
    >>> sort_letters('')
    ''
    >>> sort_letters('aba')
    'aab'
    >>> sort_letters('abcabccba')
    'aaabbbccc'

    """
    if not text:
        return text

    let = {}  #Создаю словарь, чтобы узнать сколько раз встречается буква
    for elem in text:
        if elem in let:
            let[elem] += 1
            continue
        let[elem] = 1


    #Создаю отсортированный список, чтобы буквы шли по очереди как в изначальном тексте
    result = []
    for char in text:
        if char * let[char] not in result:
            result.append(char * let[char])

    v = merge_sorted_lens(result)

    return ''.join(v)
