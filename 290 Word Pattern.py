class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        if len(pattern) != len(s): return False
        
        patternMap = {}
        for i, c in enumerate(pattern):
            if c not in patternMap:
                if s[i] in patternMap.values(): return False
                patternMap[c] = s[i]
            else:
                if patternMap[c] != s[i]:
                    return False
        return True

# Time complexity: O(m + n)
# Space complexity: O(n)