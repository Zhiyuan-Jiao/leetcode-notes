class Solution:
    def maxArea(self, height: List[int]) -> int:
        if not height: return 0

        maxArea = 0
        l, r = 0, len(height) - 1
        while l < r:
            maxArea = max(maxArea, min(height[l], height[r]) * (r - l))
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
        return maxArea

# Algorithm: two pointer, move the smaller pointer to find the max area
# Time complexity: O(n)
# Space complexity: O(1)