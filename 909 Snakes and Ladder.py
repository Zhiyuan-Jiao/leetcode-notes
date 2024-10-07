class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        board.reverse()
        length = len(board)

        def intToPos(n):
            n -= 1
            r = n // length
            c = n % length
            if r % 2:
                c = length - 1 - c
            return [r, c]

        q = collections.deque()
        q.append((1, 0))  # (position, moves)
        visited = set()
        
        while q:
            n, moves = q.popleft()
            for i in range(1, 7):
                next_n = n + i
                next_moves = moves + 1
                if next_n > length * length: continue # past destination
                r, c = intToPos(next_n)
                if board[r][c] != -1: 
                    next_n = board[r][c]
                if next_n == length * length: return next_moves # at destination
                if next_n not in visited:
                    q.append((next_n, next_moves))
                    visited.add(next_n)
        return -1

# T: O(n^2) S: O(n^2)
# Note: use bfs to find shortest path, use set to track visited cell to eliminate duplicate checks