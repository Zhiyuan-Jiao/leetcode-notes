class Solution:
    def customSortString(self, order: str, s: str) -> str:
        count = Counter(s)
        res = ""
        for c in order:
            if c not in count: continue
            while count[c] > 0:
                res += c
                count[c] -= 1
        for c in count:
            while count[c] > 0:
                res += c
                count[c] -= 1
        return res
# T: O(n + m) S: O(n)