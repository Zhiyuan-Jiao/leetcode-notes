class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0
        for n in nums:
            temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2

#  [1,     2,        3,           1]
#    ^     ^         ^            ^      
#   1,   2 > 1,  3 + 1 > 2,   2 + 1 < 4
#   1,     2,        4,           4
#  rob1,  rob2,     temp  

# Time complexity: O(n)
# Space complexity: O(1)