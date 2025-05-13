class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        hor = [[0] * cols for r in range(rows)]
        ver = [[0] * cols for r in range(rows)]

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0: continue
                hor[r][c] = hor[r][c - 1] + 1 if c > 0 else 1
                ver[r][c] = ver[r - 1][c] + 1 if r > 0 else 1
        # print(hor)
        # print(ver)

        res = 0
        for r in range(rows - 1, -1, -1):
            for c in range(cols - 1, -1, -1):
                if grid[r][c] == 0: continue
                curMax = min(hor[r][c], ver[r][c])
                while curMax > res and r - curMax + 1 >= 0 and c - curMax + 1 >= 0:
                    if min(hor[r - curMax + 1][c], ver[r][c - curMax + 1]) >= curMax:
                        res = curMax
                    curMax -= 1
        return res * res