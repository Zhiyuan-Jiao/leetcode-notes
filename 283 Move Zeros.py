class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = -1
        for j in range(len(nums)):
            if nums[j] == 0:
                if i == -1:
                    i = j
            elif i != -1:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        return nums

# T: O(n) S: O(1)
# Note: two pointers, one to track the place to modify, one to iterate