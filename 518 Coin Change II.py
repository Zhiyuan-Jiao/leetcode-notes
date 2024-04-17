class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [[0 for c in range(amount + 1)] for r in range(len(coins) + 1)]
        dp[0][0] = 1
        for r in range(1, len(coins) + 1):
            for c in range(amount + 1):
                dp[r][c] = dp[r - 1][c] + (dp[r][c - coins[r - 1]] if c >= coins[r - 1] else 0)
        return dp[-1][-1]

# Algorithm: 2D DP
# Time complexity: O(m*n)
# Space complexity: O(m*n) (can be improved to O(n))