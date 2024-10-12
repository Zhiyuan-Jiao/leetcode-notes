class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows, cols = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * cols for r in range(rows)]
        for r in range(rows):
            for c in range(cols):
                if obstacleGrid[r][c] == 1: continue
                if r == 0 and c == 0:
                    dp[r][c] = 1
                elif r == 0:
                    dp[r][c] = dp[r][c - 1]
                elif c == 0:
                    dp[r][c] = dp[r - 1][c]
                else:
                    dp[r][c] = dp[r - 1][c] + dp[r][c - 1]
        print(dp)
        return dp[rows - 1][cols - 1]

# T: O(m*n), S: O(m*n)
# Note: DP