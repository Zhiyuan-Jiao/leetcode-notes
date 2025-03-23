from bisect import bisect_left

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # res = [0]
        # def dfs(cur, nums):
        #     if not nums:
        #         if len(cur) > res[0]: 
        #             res[0] = len(cur)
        #         return 
            
        #     if len(cur) > res[0]: 
        #         res[0] = len(cur)

        #     for i, n in enumerate(nums):
        #         if n > cur[-1]:
        #             cur.append(n)
        #             dfs(cur, nums[i + 1:])
        #             cur.pop()

        # LIS = [1] * len(nums)
        # for i in range(len(nums) - 1, -1, -1):
        #     cur = LIS[i]
        #     for j in range(i + 1, len(nums)):
        #         if nums[j] > nums[i]:
        #             cur = max(cur, LIS[i] + LIS[j])
        #     LIS[i] = cur
        # return max(LIS)
        #
        # T: O(n^2) S:O(n)
        # Note: Using DP calculate max len from the right side

        LIS = []
        for n in nums:
            if not LIS:
                LIS.append(n)
                continue
            if n > LIS[-1]:
                LIS.append(n)
            else:
                index = bisect_left(LIS, n)
                LIS[index] = n
        return len(LIS)

        # T: O(Nlogn) S: O(N)
        # Note: Use a list to track the LIS, if a num is larger 
        # than the end, add it. else replace the num position in 
        # the list kind of like remember the head but still track 
        # the len of the longest so far.