class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {} # (i, total) -> # of ways
        def dfs(i, total):
            # Base case
            if i == len(nums):
                return 1 if total == target else 0
            if (i, total) in dp:
                return dp[(i, total)]
            dp[(i, total)] = dfs(i + 1, total + nums[i]) + dfs(i + 1, total - nums[i])
            return dp[(i, total)]

        return dfs(0, 0)

# Algorithm: DP 0/1 knapsack
# Time complexity: O(n*t) because of (i, total)
# Space complexity: O(n)