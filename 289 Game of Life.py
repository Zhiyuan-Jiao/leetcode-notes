class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols = len(board), len(board[0])
        dirs = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]

        for r in range(rows):
            for c in range(cols):
                liveNei = 0
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if nr in range(rows) and nc in range(cols) and board[nr][nc] > 0:
                        liveNei += 1
                if board[r][c] == 1 and (liveNei < 2 or liveNei > 3):
                    board[r][c] = 2
                elif board[r][c] == 0 and liveNei == 3:
                    board[r][c] = -1
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == -1:
                    board[r][c] = 1
                elif board[r][c] == 2:
                    board[r][c] = 0

# Note: modify in place, change dying cell to 2 and new born cell to -1
# T: O(m*n) S: O(1)