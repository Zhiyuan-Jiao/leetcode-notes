class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # dp = {} # (i, buying) -> max profit
        # def dfs(i, buying):
        #     # Base case
        #     if i >= len(prices):
        #         return 0
        #     if (i, buying) in dp:
        #         return dp[(i, buying)]
            
        #     if buying: # buy or not buy
        #         dp[(i, buying)] = max(dfs(i + 1, not buying) - prices[i], dfs(i + 1, buying))
        #     else:
        #         dp[(i, buying)] = max(dfs(i + 1, not buying) + prices[i], dfs(i + 1, buying))
        #     return dp[(i, buying)]
        # return dfs(0, True)

        l = 0
        res = 0
        for r in range(len(prices)):
            if r == l: continue
            if prices[r] < prices[r - 1]:
                res += prices[r - 1] - prices[l]
                l = r
            elif r == len(prices) - 1:
                res += prices[r] - prices[l]
        return res

        # Algorithm: two pointer
        # Time complexity: O(n)
        # Space complexity: O(1)
            