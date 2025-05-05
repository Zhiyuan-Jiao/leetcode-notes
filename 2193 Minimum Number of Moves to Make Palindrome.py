class Solution:
    def minMovesToMakePalindrome(self, s: str) -> int:
        s = list(s)
        n = len(s)
        count = 0
        
        left, right = 0, len(s) - 1
        while left <= right:
            if s[left] != s[right]:
                i = left
                j = right

                while s[left] != s[j]:
                    j -= 1
                while s[right] != s[i]:
                    i += 1

                if right - j < i - left:
                    count += right - j
                    # move s[j] to s[right]
                    for x in range(j, right):
                        s[x], s[x + 1] = s[x + 1], s[x]
                else:
                    count += i - left
                    # move s[i] to s[left]
                    for x in range(i, left, -1):
                        s[x], s[x - 1] = s[x - 1], s[x]
            left, right = left + 1, right - 1
        return count
