class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # if not nums: return 0
        # nums = sorted(nums)
        # cur = 1
        # res = 0
        # for i in range(1, len(nums)):
        #     delta = nums[i] - nums[i - 1]
        #     if delta == 1:
        #         cur += 1
        #     elif delta < 0 or delta > 1:
        #         res = max(res, cur)
        #         cur = 1
        # res = max(res, cur)
        # return res

# T: O(nlogn + n) = O(nlogn) S: O(n)

        nums = set(nums)
        res = 0
        for n in nums:
            if n - 1 not in nums:
                curLen = 1
                while n + curLen in nums:
                    curLen += 1
                res = max(curLen, res)
        return res

# T: O(n) S: O(n)