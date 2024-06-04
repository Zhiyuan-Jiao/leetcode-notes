class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1: return 0
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if m > 0 and nums[m - 1] > nums[m]:
                r = m - 1
            elif m < len(nums) - 1 and nums[m + 1] > nums[m]:
                l = m + 1
            else:
                return m

# Note: Binary Search, only need to check side with greater values
# T: O(logn) S: O(1)