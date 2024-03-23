class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols = len(board), len(board[0])
        notFlip = set()
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def dfs(r, c):
            # base case
            if board[r][c] == "X": return

            notFlip.add((r, c))

            for dir in dirs:
                nr, nc = r + dir[0], c + dir[1]
                if nr in range(rows) and nc in range(cols) and board[nr][nc] == "O" and (nr, nc) not in notFlip:
                    dfs(nr, nc)



        for c in range(cols):
            dfs(0, c)
            dfs(rows - 1, c)
        for r in range(rows):
            dfs(r, 0)
            dfs(r, cols - 1)
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O" and (r, c) not in notFlip:
                    board[r][c] = "X"
        return board

# Time complexity: O((m+n)* m*n)
# Space complexity: O(n)