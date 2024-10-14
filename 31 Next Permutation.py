class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pivot = -1
        for i in range(len(nums) - 1, 0, -1):
            if nums[i] > nums[i - 1]:
                pivot = i - 1
                break
        else:
            nums.reverse()
            return
        
        n = len(nums) - 1
        while nums[n] <= nums[pivot]:
            n -= 1
        nums[n], nums[pivot] = nums[pivot], nums[n]
        nums[pivot + 1:] = sorted(nums[pivot + 1:])

# T: O(N) S: O(1)
# Note: 1. Find the pivot which is the first number not in descending order from left 
#       2. Find the number to swap with, which is the first number larger than the pivot from left
#       3. Swap
#       4. Sorted the numbers after the pivot number