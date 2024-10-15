class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i, n in enumerate(nums):
            if not i: continue
            if (i % 2 and n < nums[i - 1]) or (not i % 2 and n > nums[i - 1]):
                nums[i - 1], nums[i] = nums[i], nums[i - 1]

# T: O(N), S: O(1)
# Note: Just swap incorrect order pair will make sure the pattern