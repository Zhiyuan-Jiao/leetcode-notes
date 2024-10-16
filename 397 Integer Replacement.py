class Solution:
    def integerReplacement(self, n: int) -> int:
        dp = {} # n -> min operations for n
        dp[0], dp[1] = 0, 0
        def recur(n):
            # base case
            if n in dp: return dp[n]

            if n % 2:
                dp[n] = 1 + min(recur(n + 1), recur(n - 1))
            else:
                dp[n] = 1 + recur(n // 2)
            return dp[n]
        return recur(n)
# T: O(n) S: (n)
# Note: DP