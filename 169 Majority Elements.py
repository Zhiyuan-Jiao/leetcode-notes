class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res, count = 0, 0
        for n in nums:
            if count == 0:
                res = n
            count += (1 if n == res else -1)
        return res

# Algorithm: reduce the count if the current num is not the num in record, change record num if count = 0
# Time complexity: O(n)
# Space complexity: O(1)