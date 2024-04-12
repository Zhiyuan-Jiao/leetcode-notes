class Solution:
    def reverse(self, x: int) -> int:
        MIN, MAX = -2 ** 31, 2 ** 31 - 1
        res = 0
        while x:
            digit = int(math.fmod(x, 10))
            x = int(x / 10)
            if res > MAX // 10 or res == MAX // 10 and digit > MAX % 10:
                return 0
            if res < int(MIN / 10) or res == int(MIN / 10) and digit < math.fmod(MIN, 10):
                return 0
            res = res * 10 + digit
        return res

# Note: python need to use int(math.fmod(x, 10)) to get last digit for negative values and truncate need to use int(x / 10)
# Time complexity: O(n)
# Space complexity: O(1)