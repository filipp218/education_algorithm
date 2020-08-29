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

    number = 0
    place = {}
    let = {}  #Создаю словарь, чтобы узнать сколько раз встречается буква
    for elem in text:
        if elem in let:
            let[elem] += 1
            continue
        let[elem] = 1
        place[elem] = number
        number += 1

    result = [0] * len(place) # Создаю пустой список с количеством букв
    for elem in let:
        result[place[elem]] = elem * let[elem]  #('abcabccba') делаю из этой строки, такой список ['aaa', 'bbb', 'ccc']
    sorter = []
    for i in let:
        sorter.append([- let[i], place[i]])  #делаю список, где [ [ - (сколько раз встретилась), на какой позиции стояла буква], ... ]добавляю минус, чтобы сортировка шла от самого большого числа к маленькому ('abcabccba') [[-3, 2], [-3, 0], [-3, 1]
    sorter.sort()  # получаю отсортированный список [[-3, 0], [-3, 1], [-3, 2]] где первое число сколько раз встретиилась, а второе индекс его из списка result ['aaa', 'bbb', 'ccc']
    final_result = []
    pos = 0   #для индекса в новый список
    for i in sorter:
        final_result.insert(pos , result[i[1]])  #добавляю в финальный список элементы из result, которые находятся по индексу из списка sorter [[-3, 0], [-3, 1], [-3, 2]]
        pos += 1

    return ''.join(final_result)
