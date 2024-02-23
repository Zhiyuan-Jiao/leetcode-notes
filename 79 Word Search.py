class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board: return False

        rows, cols = len(board), len(board[0])
        visited = set()

        def dfs(i, r, c):
            # base case
            if i == (len(word) - 1) and word[i] == board[r][c]:
                return True

            if word[i] == board[r][c]:
                visited.add((r, c))
                dir = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for d in dir:
                    nr, nc = r + d[0], c + d[1]
                    if nr in range(rows) and nc in range(cols) and (nr, nc) not in visited:
                        if dfs(i + 1, nr, nc): return True
                visited.remove((r, c))

            return False

        for r in range(rows):
            for c in range(cols):
                if dfs(0, r, c): return True
        return False

# Algorithm: Brute Force backtrack
# Time complexity: O(m*n*4^k)
# Space complexity: O(n)