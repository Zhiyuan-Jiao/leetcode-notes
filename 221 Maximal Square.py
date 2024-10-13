class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix: return 0

        rows, cols = len(matrix), len(matrix[0])
        dp = [[0] * cols for r in range(rows)]
        res = 0
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == "0":
                    continue
                if r == 0 or c == 0:
                    dp[r][c] = 1
                else:
                    dp[r][c] = min(dp[r - 1][c - 1], dp[r - 1][c], dp[r][c - 1]) + 1
                res = max(res, dp[r][c] * dp[r][c])
        return res
# T: O(m*n) S: O(m*n)
# Note: size of max square with based r, c is derived from it top left, top, and left cell's max square