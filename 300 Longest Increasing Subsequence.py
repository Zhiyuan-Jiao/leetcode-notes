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

        # for i in range(len(nums)):
        #     dfs([nums[i]], nums[i + 1:])
        # return res[0]

        LIS = [1] * len(nums)

        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i], 1 + LIS[j])
        return max(LIS)

# Time complexity: O(n**2)
# Space complexity: O(n)