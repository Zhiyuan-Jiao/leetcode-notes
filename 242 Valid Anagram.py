class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)

# Time complexity: O(m + n)
# Space complexity: O(m + n)