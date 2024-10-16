class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        if not g or not s:
            return 0
        g, s = sorted(g), sorted(s)
        res = 0
        for n in g[::-1]:
            if s and n <= s[-1]:
                s.pop()
                res += 1
        return res

# T: O(nlogn + mlogm) S: O(m + n)