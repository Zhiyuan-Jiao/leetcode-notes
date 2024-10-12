class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp = {} # (r, c) -> min sum from (r, c) to (-1, -1)
        rows, cols = len(grid), len(grid[0])
        dp[(rows - 1, cols - 1)] = grid[rows - 1][cols - 1]
        for r in range(rows - 2, -1, -1):
            dp[(r, cols - 1)] = dp[(r + 1, cols - 1)] + grid[r][cols - 1]
        for c in range(cols - 2, -1, -1):
            dp[(rows - 1, c)] = dp[(rows - 1, c + 1)] + grid[rows - 1][c]
        for r in range(rows - 2, -1, -1):
            for c in range(cols - 2, -1, -1):
                dp[(r, c)] = min(dp[(r + 1, c)], dp[(r, c + 1)]) + grid[r][c]
        return dp[(0, 0)]
# T: O (m*n) S: O(m*n)
# Note: DP