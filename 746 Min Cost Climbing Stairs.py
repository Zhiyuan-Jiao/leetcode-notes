class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)
        l, r = 0, 0
        for c in cost:
            temp = min(l, r) + c
            l = r
            r = temp
        return r

# Time complexity: O(n)
# Space complexity: O(1)