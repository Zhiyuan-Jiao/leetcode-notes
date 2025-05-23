class Solution:
    def minOperations(self, s: str) -> int:
        start0 = start1 = 0
        for i in range(len(s)):
            if not i % 2:
                if s[i] == "1":
                    start0 += 1
                else:
                    start1 += 1
            else:
                if s[i] == "1":
                    start1 += 1
                else:
                    start0 += 1
        return min(start0, start1)