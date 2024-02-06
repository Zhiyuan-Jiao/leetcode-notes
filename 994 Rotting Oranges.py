class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid: return -1

        q = collections.deque()
        time, fresh = 0, 0

        rows, cols = len(grid), len(grid[0])
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2: q.append((r, c))
                if grid[r][c] == 1: fresh += 1

        while q and fresh:
            for i in range(len(q)):
                r, c = q.popleft()
                dir = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dr, dc in dir:
                    nr, nc = r + dr, c + dc
                    if (nr in range(rows) and nc in range(cols) and
                        grid[nr][nc] == 1):
                        grid[nr][nc] = 2
                        q.append((nr, nc))
                        fresh -= 1
            time += 1

        return time if fresh == 0 else -1

# Time complexity: O(n)
# Space complexity: O(n)