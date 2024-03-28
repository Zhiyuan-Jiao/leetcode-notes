class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        rob1, rob2 = 0, 0
        for n in nums[:-1]:
            temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        res = rob2
        rob1, rob2 = 0, 0
        for n in nums[1:]:
            temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        return max(res, rob2)

# Time complexity: O(n)
# Space complexity: O(1)