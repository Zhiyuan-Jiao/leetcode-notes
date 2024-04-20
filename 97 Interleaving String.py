class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # rows, cols = len(s2) + 1, len(s1) + 1
        # grid = [[0 for c in range(cols)] for r in range(rows)]
        # res = [False]

        # def dfs(r, c, i):
        #     # base case
        #     if i >= len(s3):
        #         if r == rows - 1 and c == cols - 1:
        #             res[0] = True
        #         return
        #     if c in range(len(s1)) and s3[i] == s1[c]:
        #         if c + 1 in range(cols):
        #             dfs(r, c + 1, i + 1)
        #     if r in range(len(s2)) and s3[i] == s2[r]:
        #         if r + 1 in range(rows):
        #             dfs(r + 1, c, i + 1)


        # dfs(0, 0, 0)
        # return res[0]

        # if len(s1) + len(s2) != len(s3): return False

        # dp = [[False for c in range(len(s1) + 1)] for r in range(len(s2) + 1)]
        # dp[-1][-1] = True
        # for r in range(len(s2), -1, -1):
        #     for c in range(len(s1), -1, -1):
        #         if c < len(s1) and s1[c] == s3[r + c] and dp[r][c + 1]:
        #             dp[r][c] = True
        #         if r < len(s2) and s2[r] == s3[r + c] and dp[r + 1][c]:
        #             dp[r][c] = True
        # print(dp)
        # return dp[0][0]

        if len(s1) + len(s2) != len(s3): return False
        dp = {} # (i, j) -> True/False
        def dfs(i, j):
            # Base case
            if i >= len(s1) and j >= len(s2):
                return True
            if (i, j) in dp:
                return dp[(i, j)]

            if i < len(s1) and s1[i] == s3[i + j] and dfs(i + 1, j):
                dp[(i, j)] = True
                return True
            # print(s3[i + j])
            if j < len(s2) and s2[j] == s3[i + j] and dfs(i, j + 1):
                dp[(i, j)] = True
                return True
            dp[(i, j)] = False
            return False
        return dfs(0, 0)

        # Algorithm: LCS DP
        # Time complexity: O(m * n)
        # Space complexity: O(m * n)