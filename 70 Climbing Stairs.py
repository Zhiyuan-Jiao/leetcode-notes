class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1
        for i in range(n - 1):
            temp = one
            one += two
            two = temp
        return one
            
# Algorithm: Dynamic Programming: brutal force first, found repeating substree, store them in a dp list, found that only need last two cells to compute the current
# Time complexity: O(n)
# Space complexity: O(1)