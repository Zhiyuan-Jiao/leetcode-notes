class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        countM = Counter(magazine)
        for c in ransomNote:
            if c not in countM:
                return False
            countM[c] -= 1
            if countM[c] < 0:
                return False
        return True

# Time complexity: O(n)
# Space complexity: O(26)