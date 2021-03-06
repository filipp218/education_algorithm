Расшифровка письменности Майя оказалась более сложной задачей, чем предполагалось ранними исследованиями. 
На протяжении более чем двух сотен лет удалось узнать не так уж много. 
Основные результаты были получены за последние 30 лет.

Письменность Майя основывается на маленьких рисунках, известных как значки, 
которые обозначают звуки. Слова языка Майя обычно записываются с помощью этих значков, 
которые располагаются рядом друг с другом в некотором порядке.

Одна из проблем расшифровки письменности Майя заключается в определении этого порядка. 
Рисуя значки некоторого слова, писатели Майя иногда выбирали позиции для значков, 
исходя скорее из эстетических взглядов, а не определенных правил. 
Это привело к тому, что, хотя звуки для многих значков известны, 
археологи не всегда уверены, как должно произноситься записанное слово.

Археологи ищут некоторое слово W. Они знают значки для него, 
но не знают все возможные способы их расположения. Поскольку они знают, что Вы приедете на IOI ’06, 
они просят Вас о помощи. Они дадут Вам g значков, составляющих слово W, 
и последовательность S всех значков в надписи, которую они изучают, в порядке их появления. 
Помогите им, подсчитав количество возможных появлений слова W.

Задание Напишите программу, которая по значкам слова W и по последовательности 
S значков надписи подсчитывает количество всех возможных вхождений слова W в S, 
то есть количество всех различных позиций идущих подряд g значков в последовательности S, 
которые являются какой-либо перестановкой значков слова W .

Формат ввода
1 ≤ g ≤ 3 000, g – количество значков в слове W

g ≤ |S| ≤ 3 000 000 где |S| – количество значков в последовательности S

На вход программы поступают данные в следующем формате:

СТРОКА 1: Содержит два числа, разделенных пробелом – g и |S|. 
    СТРОКА 2: Содержит g последовательных символов, с помощью которых записывается слово W . 
    Допустимы символы: ‘a’-‘z’ и ‘A’-‘Z’; большие и маленькие буквы считаются различными. 
    СТРОКА 3: Содержит |S| последовательных символов, которые представляют значки в надписи. 
        Допустимы символы: ‘a’-‘z’ и ‘A’-‘Z’; большие и маленькие буквы считаются различными.

Формат вывода
Единственная строка выходных данных программы должна содержать количество возможных вхождений слова W в S.

Пример
Ввод	
4 11
cAda
AbrAcadAbRa

Вывод
2




len_word, len_seq = map(int, input().split())  # длина слова, длина последовтельности
letters = input()  # знаки нужного слова
word = {}  # ключ - знак, значение-сколько раз знак встречается в нужном слове
for i in letters:
    if i not in word:
        word[i] = 0
    word[i] += 1

seq = [i for i in input()]  # сама последовательность
result = 0
active_word = {}

# Алгоритм такой:
# 1.Иду по списку и если есть буква, которая встречается в нашем слове:
#       Добаляю её в словарь активных слов, ключ ставлю индекс а значение делаю 
#        копию слова. Чтобы понимать какие знаки и в каком количестве осталось найти
# 2. Проверяю активный словарь, и прохожусь по нему, 
#           если у слова, которое есть в активном словаре нет такого знака, 
#           то удаляю весь ключ-значение из активного словаря.
for i in range(len_seq):
    if active_word:
        for key in active_word.copy():
            if seq[i] not in active_word[key]:
                del active_word[key]
            else:
                active_word[key][seq[i]] -= 1
                if active_word[key][seq[i]] == 0:
                    del active_word[key][seq[i]]
                    if not active_word[key]:
                        result += 1
                        del active_word[key]

    if seq[i] in word:
        active_word[i] = word.copy()
        active_word[i][seq[i]] -= 1
        if active_word[i][seq[i]] == 0:
            del active_word[i][seq[i]]
print(result)
