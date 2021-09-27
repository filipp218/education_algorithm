class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        result = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1":
                    result += 1
                    search = [(i,j)]
                    while search:
                        x, y = search.pop()
                        grid[x][y] = "0"
                        if x < len(grid) - 1:
                            if grid[x + 1][y] == '1':
                                search.append((x + 1,y))
                        if x != 0:
                            if grid[x - 1][y] == '1':
                                search.append((x - 1,y))
                        if y < len(grid[0]) - 1:
                            if grid[x][y + 1] == '1':
                                search.append((x,y + 1))
                        if y != 0:
                            if grid[x][y - 1] == '1':
                                search.append((x,y - 1))
        return result
