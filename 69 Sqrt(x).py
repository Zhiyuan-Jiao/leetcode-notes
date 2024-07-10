class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x
        res = 0
        while l <= r:
            m = l + (r - l) // 2
            if m * m == x:
                return m
            elif m * m > x:
                r = m - 1
            else:
                l = m + 1
                res = m
        return res

# Note: Use Binary search to find the largest value with square operation smaller than x
# T: O(logn) S: O(1)