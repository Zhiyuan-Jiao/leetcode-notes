class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0] < nums[-1]: return nums[0]

        l, r = 0, len(nums) - 1
        while l <= r:
            if l == r or nums[l] < nums[r]: return nums[l]
            
            m = (l + r + 1) // 2

            if nums[m - 1] > nums[m]: return nums[m]
            elif nums[l] > nums[m]: r = m - 1
            else: l = m + 1

# Time complexity: O(logn)
# Space complexity: O(1)