class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        res = 0
        cols = rows = len(grid)
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        visited = set((0, 0))
        minHeap = [(grid[0][0], 0, 0)]
        while True:
            e, r, c = heapq.heappop(minHeap)
            res = max(res, e)
            if r == c == cols - 1:
                return res
            for dir in dirs:
                nr, nc = r + dir[0], c + dir[1]
                if nr in range(rows) and nc in range(cols) and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    heapq.heappush(minHeap, (grid[nr][nc], nr, nc))

# Notes: use a minHeap to retrieve the next smallest elevation when choosing the next cell
# Time complexity: O(n^2*logn)
# Space complexity: O(n^2)