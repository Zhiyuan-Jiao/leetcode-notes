class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        # res = [0]
        # def dfs(k):
        #     if k <= 0:
        #         res[0] = max(res[0], max(Counter(nums).values()))
        #         return
            
        #     for i in range(len(nums)):
        #         nums[i] += 1
        #         k -= 1
        #         dfs(k)
        #         nums[i] -= 1
        #         k += 1
        # dfs(k)
        # return res[0]

# Time complexity: O(n^k)
# Space complexity: O(k)

        nums.sort()
        l, r = 0, 0
        res, total = 0, 0
        while r < len(nums):
            total += nums[r]
            while nums[r] * (r - l + 1) > total + k: # goal > cur + buget
                total -= nums[l]
                l += 1
            
            res = max(res, r - l + 1)
            r += 1
        return res
# Algorithm: sort + Sliding window
# Time complexity: O(nlogn)
# Space complexity: O(1)