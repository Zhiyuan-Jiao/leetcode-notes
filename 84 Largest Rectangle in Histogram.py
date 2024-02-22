class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if not heights:
            return 0

        stack = []
        maxArea = 0
        for i, h in enumerate(heights):
            start = i
            # pop stack if curH smaller than preH
            # set curStart the that index
            while stack and h < stack[-1][1]:
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i - index))
                start = index
            stack.append([start, h])
        
        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))
        
        return maxArea

# Algorithm: Using a stack to track each rectangle with start index and height, pop when current h < stack[-1][1]
# Time complexity: O(n)
# Space complexity: O(n)