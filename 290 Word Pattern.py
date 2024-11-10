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

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        if len(pattern) != len(s): return False
        patternMap = dict()
        used = set()
        for i in range(len(pattern)):
            if pattern[i] in patternMap:
                if patternMap[pattern[i]] != s[i]:
                    return False
            else:
                if s[i] in used:
                    return False
                patternMap[pattern[i]] = s[i]
                used.add(s[i])
        return True