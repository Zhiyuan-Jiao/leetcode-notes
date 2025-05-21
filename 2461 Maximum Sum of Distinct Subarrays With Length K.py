class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        # if len(set(nums)) == len(nums):
        #     return len

        l = 0
        window = set()
        curSum = 0
        res = 0
        for r in range(len(nums)):
            while (nums[r] in window or len(window) >= k) and l < r:
                window.remove(nums[l])
                curSum -= nums[l]
                l += 1
            window.add(nums[r])
            curSum += nums[r]
            if len(window) == k:
                res = max(res, curSum)
        return res