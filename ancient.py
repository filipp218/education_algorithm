"""
Формат входных данных
В первой строке входных данных содержится целое число n - число классов.

В следующих n строках содержится описание наследования классов. В i-й строке указано от каких классов наследуется i-й класс. Обратите внимание, что класс может ни от кого не наследоваться. Гарантируется, что класс не наследуется сам от себя (прямо или косвенно), что класс не наследуется явно от одного класса более одного раза.

В следующей строке содержится число q - количество запросов.

В следующих q строках содержится описание запросов в формате <имя класса 1> <имя класса 2>.
Имя класса – строка, состоящая из символов латинского алфавита, длины не более 50.

Формат выходных данных
Для каждого запроса выведите в отдельной строке слово "Yes", если класс 1 является предком класса 2, и "No", если не является.

Sample Input:
4
A
B : A
C : A
D : B C
4
A B
B D
C D
D A
Sample Output:
Yes
Yes
Yes
No
"""



def check(family_book, child, ancient):
    if child == ancient:
        return ('Yes')
    elif child not in family_book:
        return ('Yes')
    elif family_book[child] == None:
        return ('No')
    elif ancient in family_book[child]:
        return ('Yes')
    elif ancient not in family_book[child] and family_book[child]:
        for i in family_book[child]:
            if check(family_book, i, ancient) == 'Yes':
                return ('Yes')
        return ('No')

n = int(input())
family_book = {}
for j in range(n):
    a = [i for i in input().split()]
    if len(a) == 1:
        family_book[a[0]] = None
        continue
    family_book[a[0]] = {i for i in a[1:] if i != ":"}
n = int(input())
while (n):
    ancient, child = [i for i in input().split(" ")]
    print(check(family_book, child, ancient))
    n -= 1
