from collections import deque

def condidates(x,y, board):
    result = []
    if x != len(board) - 1:
        result.append((x+1, y))
    if y != len(board[x]) - 1:
        result.append((x, y + 1))
    # if x != 0:
    #     result.append((x-1, y))
    # if y != 0:
    #     result.append((x, y-1))
    return result

a = [
    [4, 2, 3, 7],
    [2, 4, 1, 0],
    [3, 2, 10, 5]
]

b = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]

def deeykster(a):
    qu = deque()
    dict_table = {(0,0): a[0][0]}
    qu.append((0,0))

    while qu:
        x,y = qu.popleft()
        sosedi = condidates(x,y, a)
        for h,w in sosedi:
            price = a[h][w] + dict_table[(x, y)]
            if (h,w) not in dict_table:
                dict_table[(h,w)] = price
                qu.append((h, w))
            else:
                if dict_table[(h,w)] > price:
                    dict_table[(h, w)] = price
                    qu.append((h,w))
    return dict_table[(len(a)-1, len(a[0])-1)]

print(deeykster(a), 15)
print(deeykster(b), 7)
