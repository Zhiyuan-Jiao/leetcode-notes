class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pac, atl = set(), set()

        rows, cols = len(heights), len(heights[0])
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def dfs(r, c, ocean):
            ocean.add((r, c))

            for dir in dirs:
                nr, nc = r + dir[0], c + dir[1]
                if (nr in range(rows) and nc in range(cols) and
                    heights[nr][nc] >= heights[r][c] and 
                    (nr, nc) not in ocean):
                    dfs(nr, nc, ocean)
        

        for c in range(cols):
            dfs(0, c, pac)
            dfs(rows - 1, c, atl)
        
        for r in range(rows):
            dfs(r, 0, pac)
            dfs(r, cols - 1, atl)
        
        res = []
        for r in range(rows):
            for c in range(cols):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])
        return res


# Notes: use the side row (0 & rows-1) and cols (0 & cols-1) to trace back to 
# add all the cells can flow into a specific ocean into a set

# Time complexity: O((n+m)*m*n)
# Space complexity: O(m*n)