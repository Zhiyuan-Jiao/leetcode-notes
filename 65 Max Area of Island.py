class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        rows, cols = len(grid), len(grid[0])
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        def dfs(r, c):
            grid[r][c] = 0
            output = 1
            for dir in dirs:
                nr, nc = r + dir[0], c + dir[1]
                if nr in range(rows) and nc in range(cols) and grid[nr][nc] == 1:
                    output += dfs(nr, nc)
            return output
        

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    res = max(res, dfs(r, c))
        return res


# Time complexity: O(m*n)
# Space complexity: O(1)