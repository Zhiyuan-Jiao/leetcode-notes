class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        prefix = 1
        for i in range(len(res)):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for j in range(len(res) - 1, -1, -1):
            res[j] *= postfix
            postfix *= nums[j]
        return res
 
 # Algorithm: calculate the prefix and postfix result while looping the response list
 # Time complexity: O(n)
 # Space complexity exclude the response list: O(1)