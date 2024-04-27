class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = {} # (i, j) -> # of distinct subsequences when comparing s[:i + 1] to t[:t + 1]

        def dfs(i, j):
            # base case
            if j == len(t): return 1
            if i == len(s): return 0
            if (i, j) in dp: return dp[(i, j)]

            if s[i] == t[j]:
                dp[(i, j)] = dfs(i + 1, j + 1) + dfs(i + 1, j)
            else:
                dp[(i, j)] = dfs(i + 1, j)
            return dp[(i, j)]

        return dfs(0, 0)

# Algorithm: DP LCS
# Note: bottom up compute from lower right based on the optimum structure
# Time complexity: O(m*n)
# Space complexity: O(m*n)