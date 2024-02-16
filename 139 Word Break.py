class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True
        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                if i + len(w) <= len(s) and s[i:i + len(w)] == w:
                    dp[i] = dp[i + len(w)]
                if dp[i]:
                    break
        return dp[0]

# Notes: dp bottom up from the right side reminder part

# l e e t c o d e
#                 ^
# 0 1 2 3 4 5 6 7 8
# dp[8] = True : no leftover

# l e e t c o d e
#           ^
# 0 1 2 3 4 5 6 7 8
# At index 5, leftover "ode" not in wordDict
# dp[7] = dp[6] = dp[5] = False

# l e e t c o d e
#         ^       ^
# 0 1 2 3 4 5 6 7 8
# At index 4, "code" in wordDict & nothing left after code
# dp[4] = dp[4 + len("code")] = dp[8] = True

# l e e t c o d e
#   ^ ^ ^
# 0 1 2 3 4 5 6 7 8
# dp[3] = dp[2] = dp[1]

# l e e t c o d e
# ^
# 0 1 2 3 4 5 6 7 8
# At index 0, check for w in dict and leftover part
# dp[0] = dp[0 + len("leet")] = dp[4] = True