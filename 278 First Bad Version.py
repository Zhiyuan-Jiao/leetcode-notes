# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 1
        right = n
        while left <= right:
            mid = (right + left) // 2
            if (isBadVersion(mid) and mid == 1) or (isBadVersion(mid) and not isBadVersion(mid - 1)):
                return mid
            elif isBadVersion(mid):
                right = mid - 1
            else:
                left = mid + 1

# Algorithm: Binary Search
# Time complexity: O(logn)
# Space complexity: O(1)