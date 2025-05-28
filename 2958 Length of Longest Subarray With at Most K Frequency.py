class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        cntMap = defaultdict(int)
        res = 0
        l = 0
        for r in range(len(nums)):
            cntMap[nums[r]] += 1
            while cntMap[nums[r]] > k:
                cntMap[nums[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res

        # cntMap = defaultdict(int)
        # res = 0
        # l = r = 0
        # while l <= r < len(nums):
        #     cntMap[nums[r]] += 1
        #     if cntMap[nums[r]] > k:
        #         cntMap[nums[l]] -= 1
        #         l += 1
