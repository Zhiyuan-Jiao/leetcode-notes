class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        def satisfy(n):
            count = 0
            i = 0
            while i < len(nums):
                if nums[i] <= n:
                    count += 1
                    i += 2
                    if count >= k: return True
                else:
                    i += 1
            return False


        l, r = min(nums), max(nums)
        res = r
        while l <= r:
            m = l + (r - l) // 2
            if satisfy(m):
                res = m
                r = m - 1
            else:
                l = m + 1
        return res