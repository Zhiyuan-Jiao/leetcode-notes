class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        res = 0
        sign = 0
        for i, n in enumerate(nums[1:]):
            difference = n - nums[i]
            if not difference: continue
            if not sign:
                sign = -1 if difference > 0 else 1
            elif (difference > 0 and sign > 0) or (difference < 0 and sign < 0):
                sign = -1 if sign == 1 else 1
            else:
                continue
            res += 1
        return res + 1

# T: O(n) S: O(1) 
# Note: Greedy