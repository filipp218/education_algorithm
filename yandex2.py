"""
Кодирование длин серий (RLE) — алгоритм сжатия данных, заменяющий повторяющиеся символы на один символ и число его повторов. Серией называется последовательность, состоящая из нескольких одинаковых символов (более одного). При кодировании строка одинаковых символов, составляющих серию, заменяется строкой, содержащей сам повторяющийся символ и количество его повторов.

Например, строка AAAABBB будет сжата в строку A4B3, а строка AAAAAAAAAAAAAAABAAAAA — в строку A15BA5.

Вам дана сжатая строка, найдите длину исходной строки. Длина исходной строки не превышает 1000 символов, все символы исходной строки — заглавные буквы латинского алфавита. Ограничение времени: 2 с, ограничение памяти: 264 МБ.

Формат ввода
В единственной строке входных данных содержится непустая строка. Гарантируется, что эта строка является результатом корректного RLE-сжатия некоторой строки.

Формат вывода
Выведите длину исходной строки.
"""



def len_compress(text):
    """
    >>>len_compress('A4B3')
    7
    >>>len_compress('A15BA5')
    21
    """
    alphabet = {'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M'}
    counter = 0
    digit = 0
    for i in range(len(text)):
        if text[i] in alphabet:
            if digit:
                digit = int(digit)
                counter += digit - 1
            counter += 1
            digit = ''
        else:
            digit += text[i]

    if digit:
        digit = int(digit)
        counter += digit - 1

    return counter
