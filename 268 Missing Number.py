class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums += [i for i in range(len(nums) + 1)]
        res = 0
        for n in nums:
            res = res ^ n
        return res

        # Note: using xor(^) to remove duplicate between two list
    
        return sum([i for i in range(len(nums) + 1)]) - sum(nums)

        # Note: compute the sum between the complete list and the current nums