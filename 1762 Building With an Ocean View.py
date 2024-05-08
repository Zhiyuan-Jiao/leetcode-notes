class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        # res = []
        # maxH = 0
        # for i in range(len(heights) - 1, -1, -1):
        #     if heights[i] > maxH:
        #         res.append(i)
        #         maxH = heights[i]
        # return res[::-1]

        # Time complexity: O(n) Space complexity: O(1)
    
        res = []
        for i, h in enumerate(heights):
            while res and heights[res[-1]] <= h:
                res.pop()
            res.append(i)
        return res

        # Note: check from left to see if any building in our res that has a height smaller than this height, if yes pop it
        # Time complexity: O(n)
        # Space complexity: O(1)