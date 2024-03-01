class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        inWindow = dict()
        l = 0
        for r in range(len(s)):
            inWindow[s[r]] = inWindow.get(s[r], 0) + 1

            wLen = r - l + 1
            if wLen - max(inWindow.values()) <= k:
                res = wLen
            else:
                inWindow[s[l]] -= 1
                if not inWindow[s[l]]: inWindow.pop(s[l])
                l += 1
        return res

# Note: sliding window: move window when replacement cost > k else keep expand window
# Time complexity: O(26*n) = O(n)
# Space complexity: O(26)