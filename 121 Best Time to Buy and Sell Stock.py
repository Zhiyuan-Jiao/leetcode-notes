class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        l, r = 0, 1
        while r < len(prices):
            if prices[l] > prices[r]:
                l = r
            res = max(res, prices[r] - prices[l])
            r += 1
        return res

# note: use r to traverse the list and l to record the lowest
# time complexity: O(n)
# space complexity: O(1)