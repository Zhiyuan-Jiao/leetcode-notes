class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0
        res = 0
        cur_0_count = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                cur_0_count += 1
                while cur_0_count > k:
                    if nums[l] == 0:
                        cur_0_count -= 1
                    l += 1
            res = max(res, r - l + 1)
            # print(res, l, r)
        return res