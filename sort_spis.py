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

	now = ''
	change = ''

	for i in range(len(result)):  #сортировка по длинне строки O(N**2)
		for j in range(len(result)):
			if len(result[i]) > len(result[j]):
				now, change = result[i] , result [j]
				result[j], result[i] = now, change

	return ''.join(result)
