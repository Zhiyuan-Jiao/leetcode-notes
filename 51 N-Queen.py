class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        posDiag = set() # r + c
        negDiag = set() # r - c

        res = []
        board = [["."] * n for i in range(n)]
        def dfs(r):
            # base case
            if r >= n:
                copy = ["".join(i) for i in board]
                res.append(copy)
                return
            
            for c in range(n):
                if c in col or r + c in posDiag or r - c in negDiag:
                    continue
                
                col.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)
                board[r][c] = "Q"
                
                dfs(r + 1)

                col.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)
                board[r][c] = "."

        
        dfs(0)
        return res

# Time complexity: O(n!)
# Space complexity: O(n^2)
