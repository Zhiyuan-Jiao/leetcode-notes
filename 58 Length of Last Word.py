class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # res = 0
        # l = 0
        # for r in range(len(s)):
        #     if s[r] == " " and s[r - 1] != " ":
        #         res = r - l
        #     if s[r] != " " and s[r - 1] == " ":
        #         l = r
        #     if r == len(s) - 1 and s[r] != " ":
        #         res = r - l + 1
        # return res
        return len(s.split()[-1])