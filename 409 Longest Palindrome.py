class Solution:
    def longestPalindrome(self, s: str) -> int:
        charCount = Counter(s)
        res, odd = 0, 0
        for i in charCount.values():
            if i % 2 == 0:
                res += i
            else: 
                res += (i - 1)
                odd += 1
        return res if not odd else res + 1

# Time complexity: O(n)
# Space complexity: O(n)

