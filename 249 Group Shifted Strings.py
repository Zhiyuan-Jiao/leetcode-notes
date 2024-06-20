class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        patternMap = collections.defaultdict(list)
        for s in strings:
            pattern = []
            for i in range(1, len(s)):
                pattern.append((ord(s[i]) - ord(s[i - 1])) % 26) # use %26 to get the distance between two character in a alphabet loop
            patternMap[tuple(pattern)].append(s)
        return patternMap.values()

# T: O(n*k) S: O(n*k)