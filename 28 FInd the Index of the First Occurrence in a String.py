class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # return haystack.find(needle)

        l, r = 0, len(needle) - 1
        while r < len(haystack):
            if haystack[l : r + 1] == needle:
                return l
            l, r = l + 1, r + 1
        return -1

# T: O(n) S: O(1)