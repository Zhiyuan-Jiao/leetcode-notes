class Solution:
    def jump(self, nums: List[int]) -> int:
        l, r, res = 0, 0, 0
        while r < len(nums) - 1:
            farthest = 0
            for i in range(l, r + 1):
                farthest = max(farthest, i + nums[i])
            l = r + 1
            r = farthest
            res += 1
        return res

# [2, 3, 1, 1, 4]
#  0  1  1  2  2
# l,r   ->  l  r  

# Time complexity: O(n)
# Space complexity: O(1)