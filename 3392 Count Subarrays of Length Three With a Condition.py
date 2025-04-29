class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        l, r = 0, 2
        curSum = sum(nums[:3])
        cur = 1
        res = 0
        # scan through the array
        while r < len(nums):
            if float(nums[cur]) == curSum / 3 * 2:
                res += 1
            curSum -= nums[l]
            l += 1
            r += 1
            if r < len(nums):
                curSum += nums[r]
            cur += 1
        return res

# T: O(n) S: O(1)

