class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # res = float("-inf")
        # for i in range(len(nums)):
        #     cur_nums = nums[i:] + nums[:i]
        #     cur_sum = float("-inf")
        #     for j in range(len(cur_nums)):
        #         if cur_sum <= 0:
        #             if cur_nums[j] >= 0:
        #                 cur_sum = cur_nums[j]
        #             else:
        #                 cur_sum = max(cur_sum, cur_nums[j])
        #         else:
        #             cur_sum += cur_nums[j]
        #     res = max(res, cur_sum)
        # return res

        globalMax, globalMin, curMax, curMin, total = nums[0], nums[0], nums[0], nums[0], nums[0]
        for n in nums[1:]:
            total += n
            curMax = max(curMax + n, n)
            curMin = min(curMin + n, n)
            globalMax = max(globalMax, curMax)
            globalMin = min(globalMin, curMin)
        return max(globalMax, total - globalMin) if globalMax > 0 else globalMax

# T: O(n) S: O(1)
# Note keep track of both global max and min, total - min is the max when subarray is broken in two part