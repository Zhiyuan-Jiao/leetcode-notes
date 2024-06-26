class Solution:
    def validPalindrome(self, s: str) -> bool:
        def checkPali(i, j):
            while i < j:
                if s[i] != s[j]: return False
                i += 1
                j -= 1
            return True
        
        i, j = 0, len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return checkPali(i + 1, j) or checkPali(i, j - 1)
            i += 1
            j -= 1
        return True

# Time complexity: O(n)
# Space complexity: O(1)