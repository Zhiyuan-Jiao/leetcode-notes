class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        if not grid: return island

        rows, cols = len(grid), len(grid[0])
        visit = set()

        def bfs(r, c):
            visit.add((r, c))
            q = collections.deque()
            q.append((r, c))
            while q:
                r, c = q.popleft()
                dir = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dr, dc in dir:
                    nr, nc = r + dr, c + dc
                    if (nr in range(rows) and
                        nc in range(cols) and 
                        grid[nr][nc] == "1" and
                        (nr, nc) not in visit):
                        q.append((nr, nc))
                        visit.add((nr, nc))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visit:
                    bfs(r, c)
                    islands += 1
        return islands

# Time complexity: O(n)
# Space complexity: O(n)