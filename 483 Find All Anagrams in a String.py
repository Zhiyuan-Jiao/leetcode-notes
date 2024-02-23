class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

# Brute Force

        if not p or not s: return []

        pCount = Counter(p)
        res = []
        for i in range(0, len(s) - len(p) + 1):
            sCount = Counter(s[i : i + len(p)])
            if sCount == pCount:
                res.append(i)
        return res

# Time complexity: O(m*n)
# Space complexity: O(2n)

# Sliding window

        if not p or not s: return []
        res = []
        pCount = Counter(p)
        l, r = 0, len(p) - 1
        sCount = Counter(s[l:r + 1])

        while r < len(s):
            if sCount == pCount: res.append(l)
            if r == len(s) - 1: break
            sCount[s[l]] -= 1
            l += 1
            r += 1
            sCount[s[r]] = sCount.get(s[r], 0) + 1

        return res

# Time complexity: O(m*n)
# Space complexity: O(2n)