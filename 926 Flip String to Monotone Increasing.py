class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        l = r = 0
        for i in s:
            r += 1 if i == "0" else 0
        res = float("inf")
        for j in s:
            res = min(res, r + l)
            if j == "1":
                l += 1
            else:
                r -= 1
        return min(res, l + r)