class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pastNums = {}
        for i in range(len(nums)):
            if (target - nums[i]) in pastNums:
                return [pastNums[target - nums[i]], i]
            pastNums[nums[i]] = i