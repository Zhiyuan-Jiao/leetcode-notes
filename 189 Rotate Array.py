class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1: return
        k = k % len(nums) if k >= len(nums) else k
        # temp = nums[-k:] + nums[:-k]
        # for i, n in enumerate(temp):
        #     nums[i] = n
        
        def reverse(l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
        reverse(0, len(nums) - 1)
        reverse(0, k - 1)
        reverse(k, len(nums) - 1)

# T: O(n) S: O(1)
# Note: Reverse the whole string then reverse each section
