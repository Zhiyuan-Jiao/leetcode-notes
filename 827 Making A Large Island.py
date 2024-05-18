class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        cols = rows = len(grid)
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def getArea(r, c, islandIdx):
            res = 1
            grid[r][c] = islandIdx
            q = collections.deque([(r, c)])
            while q:
                cr, cc = q.popleft()
                for d in dirs:
                    nr, nc = cr + d[0], cc + d[1]
                    if nr in range(rows) and nc in range(cols) and grid[nr][nc] == 1:
                        grid[nr][nc] = islandIdx
                        res += 1
                        q.append((nr, nc))
            return res               

        # loop through matrix to get each island area, store into the corresponding key
        islandAreas = {}
        islandIdx = -1
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    islandAreas[islandIdx] = getArea(r, c, islandIdx)
                    islandIdx -= 1
        
        # loop through all the possible 0s to calculate max area
        res = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    area = 1
                    seenIslands = set()
                    for d in dirs:
                        nr, nc = r + d[0], c + d[1]
                        if nr in range(rows) and nc in range(cols) and grid[nr][nc] in islandAreas and grid[nr][nc] not in seenIslands:
                            area += islandAreas[grid[nr][nc]]
                            seenIslands.add(grid[nr][nc])
                    res = max(res, area)
        return res if res else rows*cols

# T: O(n^2) S: O(n^2)