class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # res = [0]
        # def dfs(cur, i):
        #     # base case
        #     if i > len(prices) - 1:
        #         profit = 0
        #         for j in range(1, len(cur), 2):
        #             profit += cur[j] - cur[j - 1]
        #         if profit > res[0]: res[0] = profit
        #         return

        #     cur.append(prices[i])
        #     if len(cur) % 2 == 0: 
        #         dfs(cur, i + 2)
        #     else: 
        #         dfs(cur, i + 1)
        #     cur.pop()
        #     dfs(cur, i + 1)
        # dfs([], 0)
        # return res[0]

        # # Time complexity: O(2^n)
        # # Space complexity: O(n)
        
        dp = {} # (i, buying) -> max profit
        def dfs(i, buying):
            # base case
            if i >= len(prices):
                return 0
            if (i, buying) in dp:
                return dp[(i, buying)]

            maxProfit = 0
            if buying: # buy or not buy
                maxProfit = max(dfs(i + 1, not buying) - prices[i], dfs(i + 1, buying))
            else: # sell or not sell
                maxProfit = max(dfs(i + 2, not buying) + prices[i], dfs(i + 1, buying))    

            dp[(i, buying)] = maxProfit
            return dp[(i, buying)]
        return dfs(0, True)

# Algorithm: 0/1 knacksap DP
# Note: Use backtrack with cache
# Time complexity: O(n)
# Space complexity: O(n)