class Solution:
    def longestValidSubstring(self, word: str, forbidden: List[str]) -> int:
        forbiddenSet = set(forbidden)
        res = 0
        right = len(word) - 1
        for left in range(len(word) - 1, -1, -1):
            for k in range(left, min(left + 10, right + 1)):
                if word[left:k + 1] in forbiddenSet:
                    right = k - 1
                    break
            res = max(res, right - left + 1)
        return res

# Note: checking from right to left, If we continuously increase k and realize
# that the substring in range [i, i + k] (inclusive) is in forbidden (for the 
# first time, as we increase k), then we know that the substring in [i, i + k - 1]
# (of length k) is "valid", so right = k - 1.

# Time complexity: O(n^2)
# Space complexity: O(n)