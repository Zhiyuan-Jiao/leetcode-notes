class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start, end = -1, -1

        l, r = 0, len(nums) - 1
        while l <= r:
            m = l + (r - l) // 2
            if nums[m] == target:
                start = m
                r = m - 1
            elif nums[m] > target:
                r = m - 1
            else:
                l = m + 1
        if start == -1: return [start, end]
        
        l, r = 0, len(nums) - 1
        while l <= r:
            m = l + (r - l) // 2
            if nums[m] == target:
                end = m
                l = m + 1
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        return [start, end]

# T: O(logn) S: O(1)
# Note: Binary search