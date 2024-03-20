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

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        rows, cols = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        def dfs(r, c):
            # base case
            if grid[r][c] != "1":
                return
            
            grid[r][c] = "0"
            for dir in directions:
                nr, nc = r + dir[0], c + dir[1]
                if nr in range(rows) and nc in range(cols):
                    dfs(nr, nc)
        

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    res += 1
                    dfs(r, c)
        return res

# Time complexity: O(m*n)
# Space complexity: O(1)