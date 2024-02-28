class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(i for i in s if i.isalnum()).lower()
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]: return False
            l += 1
            r -= 1
        return True

# Time complexity: O(n)
# Space complexity: O(1)