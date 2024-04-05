class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # com1, com2 = [""], [""]
        # for c in text1:
        #     com1 += [com + c for com in com1]
        # for c in text2:
        #     com2 += [com + c for com in com2]
        # return max([len(c) for c in set(com1) & set(com2)])

        dp = [[0] * (len(text2) + 1) for i in range(len(text1) + 1)]
        # dp = [[0 for j in range(len(text2) + 1)] for i in range(len(text1) + 1)]
        # print(dp2 == dp)
        for i in range(len(text1) - 1, -1, -1):
            for j in range(len(text2) - 1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])
        return dp[0][0]

# Time complexity: O(m * n)
# Space complexity: O(m * n)