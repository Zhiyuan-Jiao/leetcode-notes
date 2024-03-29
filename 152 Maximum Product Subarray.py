class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        curMin, curMax = 1, 1
        for n in nums:
            if n == 0:
                curMin, curMax = 1, 1
            
            tmp = curMax
            curMax = max(n * curMax, n * curMin, n)
            curMin = min(n * tmp, n * curMin, n)
            res = max(res, curMax)
        return res
# Note: Use a two value to store the current min max at each position
# Time complexity: O(n)
# Space complexity: O(1)