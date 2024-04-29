class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        dp = {} # (l, r) -> max coins that can collect

        def dfs(l, r):
            # base case
            if l > r:
                return 0
            if (l, r) in dp:
                return dp[(l, r)]
            
            dp[(l, r)] = 0
            for i in range(l, r + 1):
                maxCoins = nums[l - 1] * nums[i] * nums[r + 1]
                maxCoins += dfs(l, i - 1) + dfs(i + 1, r)
                dp[(l, r)] = max(maxCoins, dp[(l, r)])
            return dp[(l, r)]
        
        return dfs(1, len(nums) - 2)

# Note: DP Bottom up, think from the last coins to burst, which will break the
# nums into two part: [leftBoundry, i - 1] & [i + 1, rightBoundry], the state will be [l, r]

# Time complexity: O(n^3)
# Space complexity: O(n^2)