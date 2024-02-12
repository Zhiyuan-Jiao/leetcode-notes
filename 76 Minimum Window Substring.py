from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t: return ""

        res, resLen = "", float("infinity")
        windowDict, tDict = {}, Counter(t)
        have, require = 0, len(tDict)
        l = 0
        for r in range(len(s)):
            c = s[r]
            # add c to window dict if it is required
            if c in tDict:
                windowDict[c] = windowDict.get(c, 0) + 1
                if windowDict[c] == tDict[c]: have += 1
            
            # keep narrow the window until requirements are not met any more
            while have == require:
                if resLen > (r - l + 1):
                    resLen = (r - l + 1)
                    res = s[l:r + 1]
                if s[l] in windowDict:
                    windowDict[s[l]] -= 1
                    if windowDict[s[l]] < tDict[s[l]]:
                        have -= 1
                l += 1
            
        return res if resLen != float("infinity") else ""

# Time complexity: O(m + n)
# Space complexity: O(m + n)
