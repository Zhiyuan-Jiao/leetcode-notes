class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = [[] for i in range(len(triangle))]
        dp[0].append(triangle[0][0])
        for r in range(1, len(triangle)):
            for c in range(len(triangle[r])):
                if c == 0:
                    dp[r].append(dp[r - 1][c] + triangle[r][c])
                elif c == len(triangle[r]) - 1:
                    dp[r].append(dp[r - 1][c - 1] + triangle[r][c])
                else:
                    dp[r].append(min(dp[r - 1][c - 1], dp[r - 1][c]) + triangle[r][c])
        return min(dp[-1])

# T: O(n) S: O(n)